"""Тест значений словаря""" 

res = {
    'success': True,
    'message': 'Hello, World!',
    'type': 0,
}

def test_valid_res():
    "Тест проверяет на валидность данных"
    assert res['success'] == True
    assert res['message'] == 'Hello, World!'
    assert res['type'] == 0

def test_check_res():
    "Тест сверяет пришедшие данные"
    assert res['success'] == True
    assert type(res['message']) is str
    assert type(res['type']) is int
    assert res['type'] > -1

