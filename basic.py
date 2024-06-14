def basic_arith(oper1,oper2,oper):
    """ Do a basic arithmetic and return oper1 oper oper2 
    oper -> ADD SUB MUL DIV """

    if oper=='ADD':
        return oper1+oper2
    elif oper=='SUB':
        return oper1-oper2
    elif oper=='MUL':
        return oper1*oper2
    elif oper=='DIV':
        try:
            oper1//oper2
        except ZeroDivisionError:
            return "Deno is zero"
        else:
            return oper1//oper2
    else:
        return "Invalid Operator"


