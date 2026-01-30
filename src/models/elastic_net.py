import pandas as pd
from sklearn.linear_model import ElasticNet

def fit_elastic_net(X_train, y_train, alpha=0.01, l1_ratio=0.5):
    """
    Fit Elastic Net to predict next-month returns.
    X_train: DataFrame (rows = stocks, cols = features)
    y_train: Series (rows = stocks, values = next-month returns)
    """
    model = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, fit_intercept=True, max_iter=5000)
    model.fit(X_train.values, y_train.values)
    return model

def predict_elastic_net(model, X_test):
    """Predict scores for next-month returns."""
    return pd.Series(model.predict(X_test.values), index=X_test.index)