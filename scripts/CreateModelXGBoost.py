from Create_models import CreateModel

import mlflow

from urllib.parse import urlparse

from sklearn.metrics import mean_squared_error, accuracy_score, log_loss

import numpy as np

class CreateModelXGBoost(CreateModel):
    def callAutoLog(self):
        # mlflow.sklearn.autolog()
        mlflow.xgboost.autolog(silent=True)
    def logger(self,model,X_test, y_test,title):
        pred = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, pred))
        loss=log_loss(y_test,pred)
        acc = accuracy_score(y_test, pred)


        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("log_loss", loss)

        mlflow.log_metric("accuracy", acc)

        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        if tracking_url_type_store != "file":
            mlflow.xgboost.log_model(model, "model", registered_model_name=title)
        # else:
            mlflow.xgboost.log_model(model, "model")