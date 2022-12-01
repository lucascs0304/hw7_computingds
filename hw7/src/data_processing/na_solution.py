# Removing NaN in specific columns

# packages needed

#.c Remove those rows that contain NaN values in the columns: age, gender, ethnicity
def c_function(df, columns):
    df = df.dropna(subset=columns)
    return df


# Filling NAs with the mean in specific columns

# packages needed
import numpy as np

#d. Fill NaN with the mean value of the column in the columns: height, weight.
def d_function(df, column):
    df[column] = df[column].fillna(np.mean(df[column]))
    return df

