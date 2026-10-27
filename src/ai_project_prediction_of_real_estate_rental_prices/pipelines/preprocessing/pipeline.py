from kedro.pipeline import Pipeline, node
from .nodes import clean_data, split_data, scale_data

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=clean_data,
            inputs="raw_data",
            outputs="clean_data",
            name="clean_data_node"
        ),
        node(
            func=split_data,
            inputs="clean_data",
            outputs=["train", "val", "test"],
            name="split_data_node"
        ),
        node(
            func=scale_data,
            inputs=["train", "val", "test"],
            outputs="scaled_data",
            name="scale_data_node"
        ),
    ])
