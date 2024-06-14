def fuzzy_mather(oper1,op,oper2):
    """ Returns fuzzy math on oper1 and oper2 """

    if type(oper1) != int or type(oper2) != int:
        raise Exception("Only integer values accepted for operands ! ")
    
    if op=='+':
        result = oper1+oper2
    elif op=='-':
        result = oper1-oper2
    else:
        raise Exception("Invalid operator provided. Only + or - allowed !")
    
    if result < 0:
        return 'Negatif number !'
    elif result < 10:
        return 'Small number '
    else:
        return 'Very large number '