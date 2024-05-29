import re

def cnt_digits_letters_spaces(sentence):
    """ Count the number of digits letters and spaces in a given string """
    digCnt=re.sub("[^0-9]","",sentence)
    letterCnt=re.sub("[^a-zA-Z]","",sentence)
    spaceCnt=re.findall("[ \n]",sentence)

    print(len(digCnt))
    print(len(letterCnt))
    print(len(spaceCnt))


cnt_digits_letters_spaces('my name is shankar 555')