import predict

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
