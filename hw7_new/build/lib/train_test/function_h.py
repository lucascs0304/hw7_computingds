# Predicting the targets for train and test sets

# packages required
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# h. Predict the targets for both the train and test sets and add the prediction as a new column (use
# predict_proba from the model to get the predicted probabilities) name the new column something
# like predictions.
def h_function(X_train, X_test, features_col, fit_rf_model):
    y_train_pred = np.squeeze(fit_rf_model.predict_proba(X_train[features_col])[:, 1])
    y_test_pred = np.squeeze(fit_rf_model.predict_proba(X_test[features_col])[:, 1])
    X_train['predictions'] = y_train_pred
    X_test['predictions'] = y_test_pred
    return y_train_pred, y_test_pred