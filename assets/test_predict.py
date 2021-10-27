import predict

def test_load():
    res = predict.get_data()
    assert res.shape == (2930, 82)
