# Creating dummy variable and adding it into a dataset

# packages needed
import pandas as pd

#e. Generate dummies for ethnicity column (One hot encoding).
#def e_function(df, column):
#    dummies = pd.get_dummies(df[column], prefix=column)
#    return
def e_function(df: pd.DataFrame, cols: list):
    dummies_df = pd.get_dummies(df, columns=cols)
    return dummies_df
    


# Transforming a categorical value that assumes only two values
# into a binary variable

# packages needed

# f. Create a binary variable for gender M/F.
def f_function(df, variable):
    df[variable] = df[variable].map(dict(M=1, F=0))


