from PyQt4 import QtGui


class Box(QtGui.QLabel):

    def __init__(self, parent=None, symbol='#'):
        super(Box, self).__init__(parent)

        self.is_walkable = False
        self.is_monster = False
        self.is_magic = False
        self.is_end = False
        self.is_hero = False

        self.gp = None
        self.wp = None
        self.hp = None
        self.magp = None
        self.monp = None
        self.ep = None

        self._init(symbol)

    def _init(self, symbol):

        self.gp = QtGui.QPixmap('green.png')
        self.wp = QtGui.QPixmap('wall.png')
        self.hp = QtGui.QPixmap('hero.png')
        self.magp = QtGui.QPixmap('magic.png')
        self.monp = QtGui.QPixmap('monster.png')
        self.ep = QtGui.QPixmap('end.png')

        if symbol == '#':
            self.setPixmap(self.wp)
        elif symbol == ' ':
            self.setPixmap(self.gp)
            self.is_walkable = True
        elif symbol == '$':
            self.setPixmap(self.hp)
            self.is_hero = True
            self.is_walkable = True
        elif symbol == '*':
            self.setPixmap(self.magp)
            self.is_magic = True
            self.is_walkable = True
        elif symbol == '@':
            self.setPixmap(self.monp)
            self.is_monster = True
            self.is_walkable = True
        elif symbol == 'E':
            self.setPixmap(self.ep)
            self.is_end = True
            self.is_walkable = True
