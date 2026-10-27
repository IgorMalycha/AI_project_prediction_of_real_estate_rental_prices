import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from pycaret.regression import setup, compare_models, pull

COLUMNS_TO_DROP = ["id", "title", "description"]


def clean_for_model(df: pd.DataFrame) -> pd.DataFrame:
    return df[[c for c in df.columns if c not in COLUMNS_TO_DROP]]

def train_baseline(train: pd.DataFrame, val: pd.DataFrame):
    train = clean_for_model(train)
    val = clean_for_model(val)

    X_train = train.drop(columns=["price"])
    y_train = train["price"]

    X_val = val.drop(columns=["price"])
    y_val = val["price"]

    categorical = X_train.select_dtypes(include="object").columns.tolist()
    numeric = X_train.select_dtypes(exclude="object").columns.tolist()

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "cat",
                Pipeline(
                    [
                        ("imputer", SimpleImputer(strategy="most_frequent")),
                        ("ohe", OneHotEncoder(handle_unknown="ignore", sparse_output=True)),
                    ]
                ),
                categorical,
            ),
            ("num", SimpleImputer(strategy="median"), numeric),
        ]
    )

    model = Pipeline([("prep", preprocessor), ("reg", LinearRegression())])
    model.fit(X_train, y_train)

    preds = model.predict(X_val)

    metrics = {
        "RMSE": float(mean_squared_error(y_val, preds, squared=False)),
        "MAE": float(mean_absolute_error(y_val, preds)),
        "R2": float(r2_score(y_val, preds)),
    }

    return model, metrics

def train_automl(train: pd.DataFrame, val: pd.DataFrame):

    train = clean_for_model(train)
    val = clean_for_model(val)

    imputer = SimpleImputer(strategy="most_frequent")
    X_train = pd.DataFrame(imputer.fit_transform(train.drop(columns=["price"])),
                           columns=train.drop(columns=["price"]).columns)
    X_val = pd.DataFrame(imputer.transform(val.drop(columns=["price"])),
                         columns=val.drop(columns=["price"]).columns)

    train = X_train.assign(price=train["price"])
    val = X_val.assign(price=val["price"])

    combined = pd.concat([
        train.assign(dataset="train"),
        val.assign(dataset="val")
    ], ignore_index=True)

    setup(
        data=combined,
        target="price",
        session_id=42,
        verbose=False,
        train_size=len(train) / len(combined)
    )

    best_model = compare_models()
    results = pull() 

    automl_metrics = {
        "best_model": str(results.iloc[0]["Model"]),
        "RMSE": float(results.iloc[0]["RMSE"]),
        "MAE": float(results.iloc[0]["MAE"]),
        "R2": float(results.iloc[0]["R2"]),
    }

    return best_model, automl_metrics, results


def evaluate_models(baseline_metrics: dict, automl_metrics: dict):

    comparison = {
        "baseline": {
            "RMSE": baseline_metrics["RMSE"],
            "MAE": baseline_metrics["MAE"],
            "R2": baseline_metrics["R2"],
        },
        "automl": {
            "best_model": automl_metrics["best_model"],
            "RMSE": automl_metrics["RMSE"],
            "MAE": automl_metrics["MAE"],
            "R2": automl_metrics["R2"],
        }
    }

    return comparison

def save_best_model(baseline_model, automl_model, baseline_metrics, automl_metrics):
    """Selects better model and returns the best model object for Kedro Dataset."""

    if automl_metrics["RMSE"] < baseline_metrics["RMSE"]:
        best = automl_model
        print(">>> Selected AutoML model")
    else:
        best = baseline_model
        print(">>> Selected Baseline model")

    return best
    