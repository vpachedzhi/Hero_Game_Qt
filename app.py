import sys
from HeroDisplay import Hero_Display
from PyQt4 import QtGui

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    MainWin = QtGui.QWidget()
    MainWin.setWindowTitle('Hero game')
    MainWin.resize(500, 500)
    MainWin.show()
    Hero_Displ = Hero_Display(MainWin)
    Hero_Displ.show()
    sys.exit(app.exec_())
