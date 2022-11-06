import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('设置窗口位置')
    w.resize(300, 300)
    # w.move(1000, 20)
    center_pointer = QDesktopWidget().availableGeometry().center()
    print(center_pointer)
    x = center_pointer.x()
    y = center_pointer.y()
    print(w.frameGeometry())
    print(w.frameGeometry().getRect())
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(x - width / 2, y - height / 2)
    print(x - width / 2)
    print(y - height / 2)
    w.show()
    app.exec()