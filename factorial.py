def factorial(number):
    """ Print the factorial of a given number """
    fact=1
    for x in range(1,number+1):
        fact *= x

    print(fact)


factorial(5)