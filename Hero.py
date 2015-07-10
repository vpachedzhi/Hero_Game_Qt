# Class Hero, containig all the
# current information about the hero


class Hero:

    """Hero"""

    def __init__(self, health=100, magic=0):

        self.health = health
        self.magic = magic
        self.x = None
        self.y = None

    def printH(self):
        print('Health: {0}, Magic: {1}, X: {2}, Y: {3}'.
              format(self.health, self.magic, self.x, self.y))

    def setHealth(self, num):
        if num >= 0:
            self.health = num
        else:
            self.health = 0
