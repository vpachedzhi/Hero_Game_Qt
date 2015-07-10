from PyQt4 import QtGui, QtCore
from Map import Map
from HeroDisplay import Hero_Display


class Communicate(QtCore.QObject):

    move = QtCore.pyqtSignal(QtCore.QEvent)


class MainWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()

        self.setFixedSize(640, 700)
        self.center()
        self.setWindowTitle("Hero game")
        self.vbox = QtGui.QVBoxLayout()

        self.hero_display = Hero_Display(self)
        self.board = Map(self, self.hero_display)

        self.vbox.addWidget(self.hero_display)
        self.vbox.addWidget(self.board)
        self.setLayout(self.vbox)

        self.c = Communicate()
        self.c.move[QtCore.QEvent].connect(self.board.keyPressEvent)

    def center(self):

        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def keyPressEvent(self, event):

        if event.key() == QtCore.Qt.Key_Q:
            self.close()
        else:
            self.c.move.emit(event)

    def end_game(self, string):
        self.vbox.removeWidget(self.hero_display)
        lbl = QtGui.QLabel(string, self)
        lbl.resize(20, 100)
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(20)
        lbl.setFont(font)
        self.vbox.addWidget(lbl)
        self.board.timer.stop()
