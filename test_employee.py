from employee import Employee
import pytest

@pytest.fixture
def emp_obj():
    """ Create an Employee object that can be used across all the tests """
    emp_obj=Employee('Shankar','Shunmugavel',5000)
    return emp_obj

def test_give_default(emp_obj):
    """ Validate a default raise in salary for an employee """
    emp_obj.give_raise()
    assert emp_obj.sal == 10_000

def test_give_custom_raise(emp_obj):
    emp_obj.give_raise(555)
    assert emp_obj.sal == 5_555