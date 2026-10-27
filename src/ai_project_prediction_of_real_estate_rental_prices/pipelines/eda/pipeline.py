from kedro.pipeline import Pipeline, node
from .nodes import load_and_merge_data, perform_eda

def create_pipeline(**kwargs):
    return Pipeline([
        node(
            func=load_and_merge_data,
            inputs="raw_data",
            outputs="merged_data",
            name="load_and_merge_data_node"
        ),
        node(
            func=perform_eda,
            inputs="merged_data",
            outputs=None,
            name="perform_eda_node"
        ),
    ])
