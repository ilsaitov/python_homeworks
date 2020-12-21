import pytest
from one_hot_encoder import fit_transform


def test_list_str():
    assert fit_transform(['Moscow', 'New York', 'Moscow', 'London']) == [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

def test_empty_args():
    with pytest.raises(TypeError):
        fit_transform()

def test_empty_list():
    assert fit_transform([]) == []

def test_args_int():
    with pytest.raises(TypeError):
        fit_transform(1, 2, 3, 3)
