import random

class Dice:
    def roll(self):
        x = random.randrange(1,6,1)
        y = random.randrange(1,6,1)
        return (x,y)

dice = Dice()

print(dice.roll())