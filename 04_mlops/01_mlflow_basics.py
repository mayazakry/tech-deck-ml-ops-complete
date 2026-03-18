# MLflow Fundamentals

This script covers the basics of MLflow, including setting up experiments, logging parameters, tracking metrics, and registering models.

## Experiment Setup

```python
import mlflow
import mlflow.sklearn

mlflow.set_experiment("My Experiment")

with mlflow.start_run():
    # Your ML code here
    pass
```

## Parameter Logging

```python
mlflow.log_param("param1", value1)
mlflow.log_param("param2", value2)
```

## Metric Tracking

```python
mlflow.log_metric("metric_name", metric_value)
```

## Model Registration

```python
mlflow.sklearn.log_model(model, "model_name")
```

# Additional Comments:
- Ensure MLflow is installed.
- Use an appropriate backend for tracking and storage.
