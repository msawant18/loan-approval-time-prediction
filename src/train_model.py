import mlflow
import lightgbm as lgb

def train(df):
    X = df[["holiday_count", "branch_load"]]
    y = df["days_to_approval"]

    with mlflow.start_run():
        model = lgb.LGBMRegressor(
            n_estimators=300,
            learning_rate=0.05
        )
        model.fit(X, y)

        preds = model.predict(X)
        mae = abs(preds - y).mean()

        mlflow.log_metric("mae", mae)
        mlflow.sklearn.log_model(model, "model")

