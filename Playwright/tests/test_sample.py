from  common_methods import add_two_numbers

def test_add_two_numbers():
    assert add_two_numbers(2, 3) == 5
    assert add_two_numbers(-1, 1) == 0
    assert add_two_numbers(0, 0) == 0