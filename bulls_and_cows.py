""" Bull and cows game to guess 4 letter words in English 
    We give you 10 chances to guess the word correctly 
    exact match of letter -> BULL 
    match of letter but different location -> COW """

from random import choice

wordList=['come', 'bell', 'bear', 'play', 'sing', 'bird', 'bean', 'game', 'rice', 'four', 'five', 'tree', 'keep', 'dark', 'moon', 'cool']
myWord=choice(wordList)

def bulls_cows(guess,actual):
    """ Function returns the count of bulls and cows between the guess and the actual word inputs """
    bull=0
    cow=0

    if guess==actual:
        return '4B 0C'
    else:
        gL=list(guess)
        actL=list(actual)
        for g in gL:
            if g in actL:
                if gL.index(g) == actL.index(g):
                    bull+=1
                else:
                    cow+=1
        
        return f"{bull}B {cow}C"


x=1
print(f"I have a 4 letter word in mind. Guess the word in 10 chances ")
while x < 11:
    guess=input(f"Enter your guess {x} : ")
    result=bulls_cows(guess,myWord)
    if result == '4B 0C':
        print(f"Your guess {guess} is the right answer ")
        print(f"You guessed it in {x} chances ")
        break
    else:
        print(f" Your guess {guess} -> {result}")
        #continue
    if x==10:
        print(f"You exhausted your {x} chances. The answer is {myWord}")
    x+=1