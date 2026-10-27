import os
import json
import pandas as pd
import numpy as np
from datetime import datetime

from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.inspection import permutation_importance

import matplotlib.pyplot as plt


TARGET = "price"


def evaluate_model(train: pd.DataFrame, test: pd.DataFrame, model):
    X_train = train.drop(columns=[TARGET])
    y_train = train[TARGET]

    X_test = test.drop(columns=[TARGET])
    y_test = test[TARGET]

    cv_rmse = -cross_val_score(
        model,
        X_train,
        y_train,
        scoring="neg_root_mean_squared_error",
        cv=5,
    ).mean()

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    metrics = {
        "RMSE": float(mean_squared_error(y_test, preds, squared=False)),
        "MAE": float(mean_absolute_error(y_test, preds)),
        "R2": float(r2_score(y_test, preds)),
        "CV_RMSE": float(cv_rmse),
    }

    os.makedirs("data/reporting", exist_ok=True)
    with open("data/reporting/test_metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    return model, metrics


def error_analysis_and_plots(model, train: pd.DataFrame, test: pd.DataFrame):
    X_train = train.drop(columns=[TARGET])
    y_train = train[TARGET]

    X_test = test.drop(columns=[TARGET])
    y_test = test[TARGET]

    preds = model.predict(X_test)
    errors = y_test - preds

    os.makedirs("docs/plots", exist_ok=True)

    plt.figure()
    plt.scatter(preds, errors)
    plt.axhline(0)
    plt.xlabel("Predictions")
    plt.ylabel("Errors")
    plt.tight_layout()
    plt.savefig("docs/plots/prediction_errors.png")
    plt.close()

    r = permutation_importance(
        model,
        X_test,
        y_test,
        n_repeats=10,
        random_state=42,
        scoring="neg_root_mean_squared_error",
    )

    importances = pd.Series(r.importances_mean, index=X_test.columns).sort_values(
        ascending=False
    )

    plt.figure(figsize=(8, 6))
    importances.head(15).plot(kind="bar")
    plt.tight_layout()
    plt.savefig("docs/plots/feature_importance.png")
    plt.close()

    return importances.to_dict()


def log_model_version(metrics: dict, model_name: str = "best_model.pkl", version: str = "1.0"):
    os.makedirs("data/06_reporting", exist_ok=True)

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model_name": model_name,
        "RMSE": metrics["RMSE"],
        "MAE": metrics["MAE"],
        "R2": metrics["R2"],
        "version": version,
    }

    path = "data/06_reporting/model_versions.csv"

    if os.path.exists(path):
        df = pd.read_csv(path)
        df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    else:
        df = pd.DataFrame([row])

    df.to_csv(path, index=False)

    return df
