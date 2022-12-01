# splitting the dataset in train and test

# import package
import sklearn
from sklearn.model_selection import train_test_split

#.b Splitting the data between train and test

def b_function(df, target):
    X = df.loc[:, df.columns != target]
    y = df.loc[:, [target]]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1901, train_size = .70)
    return X_train, X_test, y_train, y_test

