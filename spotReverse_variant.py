def rev_str_rev_words(sentence) -> str:
    """ Reverse the words in a given sentence and reverse the entire sentence """

    #Using Regular Method
    #revWords=[]
    #for word in sentence.split():
    #    revWords.append(word[::-1])

    #Using List Comprehension
    revWords=[word[::-1] for word in sentence.split()]
    return ' '.join(revWords[::-1])


sentence='the quick brown fox jumped over a lazy rabbit'
print(rev_str_rev_words(sentence))