import random

class Dice (object):
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randrange(1, self.sides+1)

# Die = Dice(sides = 6)
# dieroll = Die.roll()
# print(f"Die roll: {dieroll}")

class Character(object):
    def __init__(self, HP = 10, STR = 5, DMG = 2, DEF = 5, MS = 5):
        self.HP = HP
        self.STR = STR
        self.DMG = DMG
        self.DEF = DEF
        self.MS = MS

    def attack(self, target):
        target.defend(self.DMG)


    def defend(self, DMG):
        HP_DMG = max(DMG - self.DEF, 0)
        self.DEF = max(self.DEF - DMG, 0)
        if self.DEF <= 0:
            self.DEF = 0
        self.HP -= HP_DMG
        if self.HP <= 0:
            self.HP = 0
