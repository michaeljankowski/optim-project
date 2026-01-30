from sklearn.linear_model import Lasso

def fit_lasso(X, y, alpha=1e-3):
    model = Lasso(alpha=alpha, fit_intercept=True, max_iter=10000)
    model.fit(X.values, y.values)
    return model

def predict_lasso(model, X):
    return model.predict(X.values)
