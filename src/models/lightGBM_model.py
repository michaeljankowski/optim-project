from lightgbm import LGBMRegressor

def fit_lightgbm(X, y):
    model = LGBMRegressor(
        n_estimators=400,
        learning_rate=0.05,
        num_leaves=31,
        subsample=0.8,
        colsample_bytree=0.8,
        reg_lambda=1.0,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X.values, y.values)
    return model

def predict_lightgbm(model, X):
    return model.predict(X.values)