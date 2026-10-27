from kedro.pipeline import Pipeline, node
from .nodes import evaluate_model, error_analysis_and_plots, log_model_version


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=evaluate_model,
                inputs=["train_data", "test_data", "best_model"],
                outputs=["evaluated_model", "test_metrics"],
                name="evaluate_model_node",
            ),
            node(
                func=error_analysis_and_plots,
                inputs=["evaluated_model", "train_data", "test_data"],
                outputs="feature_importances",
                name="error_analysis_node",
            ),
            node(
                func=log_model_version,
                inputs="test_metrics",
                outputs="model_versions",
                name="log_model_version_node",
            ),
        ]
    )
