def is_number_pall_variant(number):
    """ Returns if a given number is a pallindrome or not - variant 
    True -> Pallindrome 
    False -> Pallindrome """

    rev=0
    numbck=number

    while number>0:
        digit = number % 10
        number = number // 10
        rev = (rev*10) + digit

    if rev==numbck:
        return True
    else:
        return False

print(is_number_pall_variant(12345))