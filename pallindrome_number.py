def is_number_pallindrome(number):
    """ Returns if a given number is a pallindrome or not 
    True -> Pallindrome 
    False -> Pallindrome """

    if number==int(''.join(list(str(number))[::-1])):
        return True
    else:
        return False

print(is_number_pallindrome(12345987))