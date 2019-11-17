import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            self.paint = True
            self.update()
        except Exception as e:
            print(e)

    def paintEvent(self, event):
        try:
            if self.paint:
                qp = QPainter()
                qp.begin(self)
                self.drawFlag(qp)
                qp.end()
        except Exception as e:
            print(e)

    def drawFlag(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(50, 50, 30, 30)
        qp.drawEllipse(200, 100, 70, 70)
        qp.drawEllipse(300, 300, 70, 70)
        qp.drawEllipse(450, 300, 70, 70)
        qp.drawEllipse(80, 300, 70, 70)
        qp.drawEllipse(40, 350, 20, 20)
        self.paint = False


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())