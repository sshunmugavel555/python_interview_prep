def fibonacci_series_until(cap):
    """ Generate the fibonacci series until the given cap limit """
    
    if cap==1:
        fib=[0]
    elif cap==2:
        fib=[0,1]
    elif cap >= 3 :
        fib=[0,1]
        for x in range(2,cap):
            fib.append(fib[x-1]+fib[x-2])
    else:
        print("Invalid Cap limit - Enter a positive value greater than 0")
        fib=[]
    
    print(fib)


fibonacci_series_until(5)