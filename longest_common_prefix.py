def long_common_prefix(list_of_words):
    """ Returns the longest common prefix from among a list of words """

    # Loop thru the list and get the smallest word - Iteration can be done only until the smallest word length
    for x in range(len(list_of_words)):
        for y in range(x+1,len(list_of_words)):
            if len(list_of_words[x]) > len(list_of_words[y]):
                list_of_words[x],list_of_words[y] = list_of_words[y],list_of_words[x]

    small=len(list_of_words[0])

    lcp=[]
    mathchFound=False

    for s in range(small):
        for t in range(1,len(list_of_words)):
            if list_of_words[0][s]==list_of_words[t][s]:
                mathchFound=True
            else:
                mathchFound=False
                break
        if mathchFound:
            lcp.append(list_of_words[0][s])
    
    print(''.join(lcp))


wordL=['pa','spam','spa','spark']
long_common_prefix(wordL)