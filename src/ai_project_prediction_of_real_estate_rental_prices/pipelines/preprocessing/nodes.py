import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def clean_data(raw_data: dict) -> pd.DataFrame:
    logger = logging.getLogger(__name__)
    parts = []

    if isinstance(raw_data, dict):
        for _, partition in raw_data.items():
            try:
                df_part = partition()
                if isinstance(df_part, pd.DataFrame):
                    parts.append(df_part)
            except Exception:
                pass

        if not parts:
            return pd.DataFrame()

        df = pd.concat(parts, ignore_index=True)

    elif isinstance(raw_data, pd.DataFrame):
        df = raw_data.copy()
    else:
        return pd.DataFrame()

    if all(col in df.columns for col in ["id", "city", "squareMeters", "price"]):
        df = df.drop_duplicates(subset=["id", "city", "squareMeters", "price"])
    else:
        df = df.drop_duplicates()

    if "floor" in df.columns and "floorCount" in df.columns:
        df.loc[df["floor"] > df["floorCount"], "floor"] = np.nan

    text_cols = df.select_dtypes(include="object").columns
    for col in text_cols:
        df[col] = df[col].astype(str).str.strip().str.lower()

    cat_cols = df.select_dtypes(include="object").columns
    for col in cat_cols:
        df[col] = df[col].replace("", "unknown").fillna("unknown")

    essential_cols = [c for c in ["city", "price", "squareMeters"] if c in df.columns]
    df = df.dropna(subset=essential_cols)

    return df


def split_data(clean_data: pd.DataFrame):
    train_val, test = train_test_split(clean_data, test_size=0.15, random_state=42)
    train, val = train_test_split(train_val, test_size=0.1765, random_state=42)
    return train, val, test


def scale_data(train: pd.DataFrame, val: pd.DataFrame, test: pd.DataFrame):
    numeric_cols = train.select_dtypes(include=["float64", "int64"]).columns.drop("price")

    scaler = StandardScaler()
    train_scaled = train.copy()
    val_scaled = val.copy()
    test_scaled = test.copy()

    train_scaled[numeric_cols] = scaler.fit_transform(train[numeric_cols])
    val_scaled[numeric_cols] = scaler.transform(val[numeric_cols])
    test_scaled[numeric_cols] = scaler.transform(test[numeric_cols])

    scaled_data = pd.concat([train_scaled, val_scaled, test_scaled], ignore_index=True)
    scaled_data.to_csv("data/primary/scaled_data.csv", index=False)

    return scaled_data
