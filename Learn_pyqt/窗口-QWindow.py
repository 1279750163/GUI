import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication

class Mywindow(QMainWindow):

    def __init__(self):
        super(Mywindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        label = QLabel('这是文字~~')
        label.setStyleSheet('font-size:30px; color:red;')

        menu = self.menuBar()
        menu.setNativeMenuBar(False)

        file_menu = menu.addMenu('文件')
        file_menu.addAction('新建')
        file_menu.addAction('打开')
        file_menu.addAction('保存')

        edit_menu = menu.addMenu('编辑')
        edit_menu.addAction('复制')
        edit_menu.addAction('粘贴')
        edit_menu.addAction('剪切')

        self.setCentralWidget(label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    app.exec()