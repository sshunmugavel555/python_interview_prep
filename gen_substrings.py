def gen_substrings(word):
    """ Generate all possible substrings of the given string - word """

    substr=[]

    x=0
    y=1
    
    while x<=len(word):
        while y<=len(word):
            substr.append(word[x:y])
            y+=1
        x+=1
        y=x+1

    print(substr)


gen_substrings('shankar')