# training a model

# packages required
import sklearn
from sklearn.ensemble import RandomForestClassifier

# g. Train a model (for instance LogisticRegression or RandomForestClassifier from sklearn) in the
# train data. Use as features the columns: ‘age’, ‘height’, ‘weight’, ‘aids’, ‘cirrhosis’, ‘hepatic_failure’,
# ‘immunosuppression’, ‘leukemia’, ‘lymphoma’, ‘solid_tumor_with_metastasis’. Use as target the
# column: ‘diabetes_mellitus’

def g_function(df, train, target):
    X_train = df.loc[:, train]
    y_train = df.loc[:, target]
    rf = RandomForestClassifier(max_depth=6, random_state=0)
    fit_rf_model = rf.fit(X_train, y_train)
    return fit_rf_model

# Predicting the targets for train and test sets

# packages required
import numpy as np
import pandas as pd
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


# Computing the results testing roc_auc

# packages required
from sklearn.metrics import roc_auc_score

# i. Compute the train and test roc_auc metric using roc_auc_score from sklearn
def i_function(input, output):
    return roc_auc_score(input, output)
