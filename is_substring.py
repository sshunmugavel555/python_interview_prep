def is_substring(word,sstring):
    """ Generate all possible substrings of the given string - word 
    check if string is a substring of the word """

    substr=[]

    x=0
    y=1
    
    while x<=len(word):
        while y<=len(word):
            substr.append(word[x:y])
            y+=1
        x+=1
        y=x+1

    if sstring in substr:
        return True
    else:
        return False


print(is_substring('shankar','sankar'))