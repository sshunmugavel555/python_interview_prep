def is_pallindrome(word):
    """ Returns if the given word is a pallindrome or not """
    word=''.join(word.split())
    if word==word[::-1]:
        return True
    else:
        return False

print(is_pallindrome('sky'))
print(is_pallindrome('malayalam'))
print(is_pallindrome("cigar to go tragic"))