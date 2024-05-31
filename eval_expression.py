""" 1. While there are still tokens to be read in,
   1.1 Get the next token.
   1.2 If the token is:
       1.2.1 A number: push it onto the value stack.
       1.2.2 A variable: get its value, and push onto the value stack.
       1.2.3 A left parenthesis: push it onto the operator stack.
       1.2.4 A right parenthesis:
         1 While the thing on top of the operator stack is not a 
           left parenthesis,
             1 Pop the operator from the operator stack.
             2 Pop the value stack twice, getting two operands.
             3 Apply the operator to the operands, in the correct order.
             4 Push the result onto the value stack.
         2 Pop the left parenthesis from the operator stack, and discard it.
       1.2.5 An operator (call it thisOp):
         1 While the operator stack is not empty, and the top thing on the
           operator stack has the same or greater precedence as thisOp,
           1 Pop the operator from the operator stack.
           2 Pop the value stack twice, getting two operands.
           3 Apply the operator to the operands, in the correct order.
           4 Push the result onto the value stack.
         2 Push thisOp onto the operator stack.
2. While the operator stack is not empty,
    1 Pop the operator from the operator stack.
    2 Pop the value stack twice, getting two operands.
    3 Apply the operator to the operands, in the correct order.
    4 Push the result onto the value stack.
3. At this point the operator stack should be empty, and the value
   stack should have only one value in it, which is the final result. """

# Function for precedence of operator
def precedence(op):
    """ Returns the precedence of a given operator """
    if op=='+' or op=='-':
        return 1
    elif op=='*' or op=='/':
        return 2
    return 0

def applyoperator(a,b,op):
    """ Perform arithmetic operation based on the operator and return result """
    if op=='+':
        return a+b
    if op=='-':
        return a-b
    if op=='*':
        return a*b
    if op=='/':
        return a//b

def evaluateExpression(tokens):
    """ Function to evaluate the input token string and return the result """

    # Stack for integer values
    values=[]

    # Stack for operators
    ops=[]

    i=0
    while i<len(tokens):

        # Parse and disregard whitespace in the string of tokens
        if tokens[i]==' ':
            i+=1
            continue
        
        # If a open paranthesis is encountered, add it to the ops stack
        elif tokens[i]=='(':
            ops.append(tokens[i])

        
        elif tokens[i].isdigit():
            val=0

            #There can be more than one digit in a given number - we need to accommodate this logic
            while (i<len(tokens) and tokens[i].isdigit()):
                val=val*10+int(tokens[i])
                i+=1
            values.append(val)

            # As i was increased inside the inner loop, it has to be decreased/reset.
            i-=1

        # Closing bracket encountered - solve the brace
        elif tokens[i]==')':

            while len(ops) !=0 and ops[-1] !='(':

                val2=values.pop()
                val1=values.pop()
                op=ops.pop()

                values.append(applyoperator(val1,val2,op))
            
            # Pop the opening brace
            ops.pop()

        # Parse the operators
        else:

            while (len(ops) !=0 and precedence(ops[-1]) >= precedence(tokens[i])):
                
                val2=values.pop()
                val1=values.pop()
                op=ops.pop()

                values.append(applyoperator(val1,val2,op))

            # push current token to ops
            ops.append(tokens[i])

        i+=1

    # Parse and Evaluate leftover operators in ops Q

    while len(ops) != 0:

        val2=values.pop()
        val1=values.pop()
        op=ops.pop()

        values.append(applyoperator(val1,val2,op))

    
    # Return final values
    return values[0]


print(evaluateExpression("100 * ( 2 + 12 ) / 14"))



        
