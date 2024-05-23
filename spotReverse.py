def spot_reverse_string(sentence) -> str:
    """ Reverse the words in a given sentence on spot without reversing the entire sentence """

    #Using Regular Method
    #revWords=[]
    #for word in sentence.split():
    #    revWords.append(word[::-1])

    #Using List Comprehension
    revWords=[word[::-1] for word in sentence.split()]
    return ' '.join(revWords)


sentence='the quick brown fox jumped over a lazy rabbit'
print(spot_reverse_string(sentence))