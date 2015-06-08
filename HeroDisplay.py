import sys
from PyQt4 import QtGui
from Hero import Hero


class Hero_Display(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setFixedSize(150, 50)
        grid = QtGui.QGridLayout()
        health_lcd = QtGui.QLCDNumber()
        magic_lcd = QtGui.QLCDNumber()
        self.hero = Hero()
        health_lcd.display(self.hero.health)
        magic_lcd.display(self.hero.magic)
        grid.addWidget(health_lcd, 0, 0)
        grid.addWidget(magic_lcd, 0, 1)

        self.setLayout(grid)
