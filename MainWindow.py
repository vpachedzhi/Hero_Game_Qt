import sys
from PyQt4 import QtGui
from Hero import Hero
from Map import Map
from HeroDisplay import Hero_Display


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        self.setFixedSize(550, 500)
        self.setWindowTitle("Hero game")
        grid = QtGui.QGridLayout()
        hero = Hero_Display(self)
        board = Map(self)
        grid.addWidget(hero, 0, 0)
        grid.addWidget(board, 1, 0)
        self.setLayout(grid)
