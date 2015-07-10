from PyQt4 import QtGui
from Hero import Hero


class Hero_Display(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Hero_Display, self).__init__(parent)

        self.setFixedSize(600, 55)

        hbox = QtGui.QHBoxLayout()
        hbox.addStretch(1)
        self.health_lcd = QtGui.QLCDNumber(self)
        self.magic_lcd = QtGui.QLCDNumber(self)

        self.lblHealth = QtGui.QLabel('Health', self)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        self.lblHealth.setFont(font)
        self.lblMagic = QtGui.QLabel('Magic', self)
        self.lblMagic.setFont(font)

        self.hero = Hero(10,0)

        self.health_lcd.display(self.hero.health)
        self.magic_lcd.display(self.hero.magic)

        hbox.addWidget(self.lblHealth)
        hbox.addWidget(self.health_lcd)
        hbox.addWidget(self.lblMagic)
        hbox.addWidget(self.magic_lcd)

        self.setLayout(hbox)
