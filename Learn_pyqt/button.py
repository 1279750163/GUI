import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('第一个PyQt程序')
    btn = QPushButton('按钮')
    btn.setParent(w)
    w.show()
    app.exec()