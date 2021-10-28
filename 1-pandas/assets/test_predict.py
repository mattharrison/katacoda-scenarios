import predict

from sklearn.model_selection import train_test_split


def test_load():
    res = predict.get_data()
    assert res.shape == (2930, 82)

def test_tweak_clf():
    df = predict.get_data()
    res = predict.tweak_ames_classification(df)
    count_missing_numbers = res.select_dtypes('number').isna().sum().sum()
    assert count_missing_numbers == 0, 'Should replace missing numbers with zero'
    count_missing_objects = res.select_dtypes('object').isna().sum().sum()
    assert count_missing_objects == 0, 'Should replace missing Electricity values'

def test_clf_transformer():
    tf = predict.AmesClassifierTransformer()
    df = predict.get_data()
    res = tf.fit(df, df['Bldg Type'])
    assert res != None, '.fit should return the instance'
    res2 = tf.transform(df)
    assert res2.shape[0] == 2930

def test_clf_pipeline():
    df = predict.get_data()
    pipeline = predict.get_clf_pipeline()
    X, y = pull_out_col(df, 'Bldg Type')
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    res = pipeline.fit(X_train, y_train)
    assert res != None, 'Unable to fit pipeline'
    res2 = pipeline.score(X_test, y_test)
    assert res2 > .5, 'Unable to score pipeline'

def pull_out_col(df, col):
    return (df.drop(columns=[col])), df[col]
