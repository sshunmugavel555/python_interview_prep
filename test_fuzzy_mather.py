import pytest
from fuzzy_mather import fuzzy_mather

class TestFuzzyMath:
    """ Class that holds test methods to test fuzzy Math logic funtion """

    def test_oper1_non_integer(self):
        error=None
        try:
            fuzzy_mather('sh','+',5)
        except Exception as e:
            error=e
        #print(error)
        assert error is not None
        

    def test_oper2_non_integer(self):
        with pytest.raises(Exception) as e:
            fuzzy_mather(5,'+','sh')
        assert 'Only integer' in str(e)

    def test_addition_with_neg_result(self):
        assert fuzzy_mather(-10,'+',5)=='Negatif number !'

    def test_addition_with_positive_result(self):
        assert fuzzy_mather(5,'+',55)=='Very large number '

    def test_addition_with_small_result(self):
        assert fuzzy_mather(5,'+',4)=='Small number '

    def test_addition_with_veryLarge_result(self):
        assert fuzzy_mather(5,'+',55)=='Very large number '

    def test_sub_with_neg_result(self):
        assert fuzzy_mather(5,'-',55)=='Negatif number !'

    def test_sub_with_positive_result(self):
        assert fuzzy_mather(55,'-',5)=='Very large number '

    def test_invalid_operator(self):
        #assert fuzzy_mather(55,'*',5)=='Very large number '
        pass

    

    
    
    