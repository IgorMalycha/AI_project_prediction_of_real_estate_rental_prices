import pandas as pd
import numpy as np

from ai_project_prediction_of_real_estate_rental_prices.pipelines.preprocessing.nodes import (
    clean_data,
    split_data,
    scale_data,
)

def sample_raw_data():
    return pd.DataFrame({
        "id": [1, 2, 3],
        "city": ["Warszawa", "Kraków", "Gdańsk"],
        "squareMeters": [40, 55, 70],
        "price": [2500, 3200, 4200],
        "floor": [2, 3, 10],
        "floorCount": [5, 10, 15],
    })


def test_clean_data_not_empty():
    df = clean_data(sample_raw_data())
    assert not df.empty


def test_clean_data_row_count():
    df = clean_data(sample_raw_data())
    assert len(df) == 3


def test_split_data_shapes():
    df = clean_data(sample_raw_data())
    train, val, test = split_data(df)

    total = len(train) + len(val) + len(test)
    assert total == len(df)


def test_scale_data_standardization():
    df = clean_data(sample_raw_data())
    train, val, test = split_data(df)
    train_scaled, val_scaled, test_scaled = scale_data(train, val, test)

    numeric_cols = ["squareMeters", "floor"]

    mean = train_scaled[numeric_cols].mean()
    std = train_scaled[numeric_cols].std()

    assert all(mean.abs() < 0.1), f"Średnia ≈ 0, ale mamy {mean}"
    assert all((std - 1).abs() < 0.1), f"Std ≈ 1, ale mamy {std}"