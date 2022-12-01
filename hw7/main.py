from src.importing_data.import_data import a_function
from src.data_processing.na_solution import c_function, d_function
from src.data_processing.create_dummies  import e_function, f_function
from src.train_test.spliting_data import b_function
from src.train_test.training_model import g_function, h_function, i_function

X_FEATURES = ['age', 'height', 'weight', 'aids', 'cirrhosis', 'hepatic_failure',
'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']

df = from_csv('sample_diabetes_mellitus_data.csv')

df = drop(df, columns_l = ['age', 'gender', 'ethnicity'])

df = fill(df, columns_l = ['height', 'weight'])

df = generate(df, columns_l = ['ethnicity'])

df = binarize(df, init_column_name='gender', binarized_column_name='M/F')

X_train, X_test, y_train, y_test = split(data=df, target='diabetes_mellitus')

trained_model = train(model='rf', X_train=X_train, y_train=y_train, X_features_l=X_FEATURES)

y_train, y_test = predict(trained_model, X_train, y_train, X_test, y_test, X_features_l=X_FEATURES)
