from random import randint

def uniq_perm(word):
    """ Print out all the unique permutations of a given string """

    uniq=[]
    wordL=list(word)

    for x in range(5000):
        ind1=randint(0,len(word)-1)
        ind2=randint(0,len(word)-1)
        wordL[ind1],wordL[ind2]=wordL[ind2],wordL[ind1]
        uniq.append(''.join(wordL))
    
    print(set(uniq))
    print(f"{len(set(uniq))} unique permutations")   


uniq_perm('ABSGE')
