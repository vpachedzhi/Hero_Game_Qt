import sys
from PyQt4 import QtGui
from PyQt4.QtGui import QColor

# Class Map


class Map(QtGui.QWidget):

    def __init__(self, parent=None, rows=0, cols=0):
        QtGui.QWidget.__init__(self, parent)
        self.setFixedSize(500, 500)
        self.setAutoFillBackground(True)
        self.rows = rows
        self.cols = cols

    def draw(self):
    	pass
