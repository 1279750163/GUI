import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle('文字编辑')

    label = QLabel('账号', w)
    label.setGeometry(20, 20, 30, 30)

    edit = QLineEdit(w)
    edit.setPlaceholderText('请输入账号')
    edit.setGeometry(55, 25, 200, 20)
    # lineedit = QLineEdit('请输入账号', w)

    btn = QPushButton('注册', w)
    btn.setGeometry(50, 60, 70, 30)

    w.show()
    app.exec()