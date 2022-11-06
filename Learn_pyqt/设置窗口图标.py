import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('设置图标')
    w.setWindowIcon(QIcon('Image/R.png'))
    w.show()
    app.exec()