from PyQt5 import uic, QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QUrl, QPointF
from PyQt5.QtGui import QPainter, QBrush, QPolygonF
import sys
import random
import math



class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_figures_Git.ui', self)
        self._im = QtGui.QImage(self.width(), self.height(), QtGui.QImage.Format_ARGB32)
        self._im.fill(QtGui.QColor("white"))
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb = (r, g, b)
        width = self.size().width()
        height = self.size().height()
        x_w = random.randint(5, width - 100)
        y_h = random.randint(5, height - 100)

        painter = QtGui.QPainter(self._im)
        painter.setPen(QtGui.QPen(QtGui.QColor("#000000"), 1, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap))
        painter.setBrush(QtGui.QBrush(QtGui.QColor(rgb[0], rgb[1], rgb[2]), QtCore.Qt.SolidPattern))
        size = random.randint(5, 100)
        painter.drawEllipse(x_w, y_h, size, size)
        # Перерисуемся
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QtGui.QPainter(self)
        painter.drawImage(0, 0, self._im)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())
