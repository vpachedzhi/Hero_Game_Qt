from PyQt4 import QtGui, QtCore
from Box import Box
from random import choice


class Communicate(QtCore.QObject):

    signal = QtCore.pyqtSignal(str)

# Class Map


class Map(QtGui.QWidget):

    magic_changed = QtCore.pyqtSignal(int)

    def __init__(self, parent=None, display=None):
        super(Map, self).__init__(parent)
        self.parent = parent
        self.hero_display = display
        self.symbolMap = self.read_txt_map()
        self.grid = QtGui.QGridLayout()
        self.board = []

        for i in range(0, 20):
            self.board.append([])
            for j in range(0, 20):
                box = Box(self, self.symbolMap[i][j])
                self.board[i].append(box)
                self.grid.addWidget(box, i, j)

        self.grid.setVerticalSpacing(0)
        self.grid.setHorizontalSpacing(0)
        self.setLayout(self.grid)

        self.find_hero()
        self.print_txt_map()

        self.c = Communicate()
        self.c.signal[str].connect(self.parent.end_game)
        self.timer = QtCore.QBasicTimer()
        self.timer.start(150, self)
        self.monstX = 0
        self.monstY = 0
        self.find_monster()

    def read_txt_map(self):

        with open('map.txt', 'r') as f:
            read_data = f.read()
            arr = read_data.split('\n')
            for i in range(0, len(arr)):
                arr[i] = list(arr[i])

            return arr

    def find_hero(self):

        for i in range(0, len(self.symbolMap)):
            for j in range(0, len(self.symbolMap[i])):
                if self.symbolMap[i][j] == '$':
                    self.hero_display.hero.x = i
                    self.hero_display.hero.y = j
                    self.symbolMap[i][j] = ' '
                    break
                    break

    def print_txt_map(self):
        for line in self.symbolMap:
            print(line)

    def collect_magic(self, box):
        if box.is_magic:
            self.hero_display.hero.magic = \
                self.hero_display.hero.magic + 1
            self.hero_display.magic_lcd.display(self.hero_display.hero.magic)
            box.is_magic = False

    def end_game(self, box):
        if box.is_end:
            self.c.signal.emit("You win !")

    def move(self, hX, hY, box1, box2):
        b = Box()
        if box2.is_walkable:
            box2.setPixmap(b.hp)
            box1.setPixmap(b.gp)

            box2.is_hero = True
            box1.is_hero = False

            self.collect_magic(box2)
            self.end_game(box2)
            return True
        else:
            return False

    def find_monster(self):
        for x in range(20):
            for y in range(20):
                if self.board[x][y].is_monster:
                    self.monstX = x
                    self.monstY = y

    def keyPressEvent(self, event):

        x = self.hero_display.hero.x
        y = self.hero_display.hero.y

        if event.key() == QtCore.Qt.Key_W:
            print('Up')
            if self.move(x, y, self.board[x][y], self.board[x - 1][y]):
                self.hero_display.hero.x = x - 1
                self.hero_display.hero.printH()

        elif event.key() == QtCore.Qt.Key_S:
            print('Down')
            if self.move(x, y, self.board[x][y], self.board[x + 1][y]):
                self.hero_display.hero.x = x + 1
                self.hero_display.hero.printH()

        elif event.key() == QtCore.Qt.Key_D:
            print('Right')
            if self.move(x, y, self.board[x][y], self.board[x][y + 1]):
                self.hero_display.hero.y = y + 1
                self.hero_display.hero.printH()

        elif event.key() == QtCore.Qt.Key_A:
            print('Left')
            if self.move(x, y, self.board[x][y], self.board[x][y - 1]):
                self.hero_display.hero.y = y - 1
                self.hero_display.hero.printH()

    def timerEvent(self, e):
        x, y = self.monstX, self.monstY
        b = Box()
        l = [-1, 0, 1]
        X = choice(l)
        Y = choice(l)
        if (X, Y) == (0, 0):
            return
        dest = self.board[x + X][y + Y]

        if dest.is_walkable and dest.is_magic is False:
            if dest.is_hero:
                self.hero_display.hero.setHealth(
                    self.hero_display.hero.health - (
                        4 - self.hero_display.hero.magic))
                self.hero_display.health_lcd.display(
                    self.hero_display.hero.health)
                if self.hero_display.hero.health == 0:
                    self.c.signal.emit('You lost')

            dest.setPixmap(b.monp)
            self.board[x][y].setPixmap(b.gp)
            self.monstX, self.monstY = x + X, y + Y
