from random import randint

def shuffle_deck(deck):
    """ Shuffle a deck of 52 cards in random order for each draw """

    for _ in range(1000):
        x=randint(0,51)
        y=randint(0,51)
        deck[x],deck[y]=deck[y],deck[x]
    
    return deck

print(f"Original Deck")
deck=list(range(1,53))
print(deck)
shuffl=shuffle_deck(deck)
print(f"After a Shuffle")
print(shuffl)