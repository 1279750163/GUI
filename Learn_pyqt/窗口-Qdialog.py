import sys
from PyQt5.QtWidgets import QDialog, QPushButton, QApplication
from PyQt5.Qt import *
class Mywindow(QDialog):

    def __init__(self):
        super(Mywindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        btn_ok = QPushButton('确定', self)
        btn_ok.setGeometry(50, 50, 100, 30)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.setWindowTitle('对话框')
    w.show()
    app.exec()