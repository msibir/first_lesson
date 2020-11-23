import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QBrush, QPen


class Second(QWidget):
    def __init__(self):
        super(Second, self).__init__()
        uic.loadUi("UI.ui", self)
        self.flag = False
        self.circles = []
        self.pushButton.clicked.connect(self.click)

    def paintEvent(self, event) -> None:
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        yellow_color = QColor.fromRgb(255, 255, 0)
        qp.setBrush(QBrush(yellow_color))
        qp.setPen(QPen(yellow_color))
        for x, y, r in self.circles:
            qp.drawEllipse(x, y, r, r)

    def click(self):
        self.flag = True
        self.circles.append((randint(0, self.geometry().width()),
                             randint(0, self.geometry().height()),
                            randint(0, 100)))
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Second()
    ex.show()
    app.exec()
