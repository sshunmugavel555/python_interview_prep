from random import randint

class Die:
    """ Class that models a Die/Dice """
    def __init__(self,sides=6) -> None:
        """ init the sides of the dice """
        self.sides=sides

    def roll_die(self):
        """ simulate dice roll """
        return randint(1,self.sides)
    

dice6=Die(6)
dice10=Die(10)

print('Rolling a 6 sided dice')
for _ in range(10):
    print(dice6.roll_die())

print('Rolling a 10 sided dice')
for _ in range(20):
    print(dice10.roll_die())



