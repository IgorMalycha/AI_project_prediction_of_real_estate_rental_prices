from kedro.pipeline import Pipeline
from ai_project_prediction_of_real_estate_rental_prices.pipelines import eda as eda_pipeline
from ai_project_prediction_of_real_estate_rental_prices.pipelines import preprocessing as preprocessing_pipeline
from ai_project_prediction_of_real_estate_rental_prices.pipelines import modeling as modeling_pipeline
from ai_project_prediction_of_real_estate_rental_prices.pipelines import evaluation as evaluation_pipeline

def register_pipelines() -> dict[str, Pipeline]:
    return {
        "eda": eda_pipeline.create_pipeline(),
        "__default__": eda_pipeline.create_pipeline(),
        "preprocessing": preprocessing_pipeline.create_pipeline(),
        "modeling": modeling_pipeline.create_pipeline(),
        "evaluation": evaluation_pipeline.create_pipeline(),  
    }
