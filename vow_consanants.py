def echo_count_of_vow_consonants(sentence):
    """ Echo the count of vowels and consonants in a given sentence """
    vowCnt=0
    conCnt=0

    vow=['a','e','i','o','u','A','E','I','O','U']

    for eW in sentence.split():
        for eL in list(eW):
            if eL in vow:
                vowCnt+=1
            else:
                conCnt+=1

    print(f"Number of vowels : {vowCnt}")
    print(f"Number of consonants : {conCnt}")


echo_count_of_vow_consonants("I Am a Big bOy")