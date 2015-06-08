# Class Hero, containig all the
# current information about the hero


class Hero:

    """Hero"""

    def __init__(self, health=100, magic=100, items=[]):
        self.items = items
        self.health = health
        self.magic = magic

    def printH(self):
        return 'Health: {0}, Items:{1}'.format(self.health, self.items)

    def is_alive(self):
        return self.health == 0
