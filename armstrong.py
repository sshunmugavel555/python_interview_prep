def is_armstrong(number):
    """ Returns if the given number is an armstrong number 

    a^n + b^n + c^n = abc ( n is the number of digits )
    """
    digCnt=0
    cnt=0

    numbck=number

    while number>0:
        number=number//10
        digCnt+=1
    
    number=numbck

    while number>0:
        dig=number%10
        number=number//10  
        cnt+=dig**digCnt

    print(cnt)
    print(numbck)
    if cnt==numbck:
        return True
    else:
        return False
    

print(is_armstrong(8209))