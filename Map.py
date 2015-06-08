import sys
from PyQt4 import QtGui

# Class Map


class Map(QtGui.QWidget):

    def __init__(self, rows, cols):
        QtGui.QWidget.__init__(self, parent)
        self.rows = rows
        self.cols = cols
