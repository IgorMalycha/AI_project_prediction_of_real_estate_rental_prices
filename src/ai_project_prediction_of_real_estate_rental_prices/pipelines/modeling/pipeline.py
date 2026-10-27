from kedro.pipeline import Pipeline, node
from .nodes import (
    train_baseline,
    train_automl,
    evaluate_models,
    save_best_model
)


def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=train_baseline,
            inputs=["train_data", "val_data"],
            outputs=["baseline_model", "baseline_metrics"],
            name="baseline_model_training"
        ),
        node(
            func=train_automl,
            inputs=["train_data", "val_data"],
            outputs=["automl_model", "automl_metrics", "automl_results"],
            name="automl_training"
        ),
        node(
            func=evaluate_models,
            inputs=["baseline_metrics", "automl_metrics"],
            outputs="model_comparison",
            name="model_evaluation"
        ),
        node(
            func=save_best_model,
            inputs=["baseline_model", "automl_model", "baseline_metrics", "automl_metrics"],
            outputs="best_model",
            name="select_and_save_best_model"
        )
    ])
