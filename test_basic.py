import pytest
from basic import basic_arith

def test_add():
    assert basic_arith(5,10,"ADD")==15
def test_sub():
    assert basic_arith(5,10,"SUB")==-5
def test_mul():
    assert basic_arith(5,0,"MUL")==0
def test_div():
    assert basic_arith(10,0,"DIV")=="Deno is zero"
def test_invOperand():
    assert basic_arith(5,5,'ADDITION')=="Invalid Operator"