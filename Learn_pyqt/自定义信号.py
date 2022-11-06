import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Mywindow(QWidget):

    my_signal = pyqtSignal(str)

    def __init__(self):
        super(Mywindow, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(500, 300)
        btn = QPushButton('开始检查', self)
        btn.setGeometry(100, 150, 100, 30)
        btn.clicked.connect(self.check)
        self.my_signal.connect(self.my_slot)

    def my_slot(self, msg):
        print('>>', msg)
    def check(self):
        for i, ip in enumerate(['192.168.1.%d' %x for x in range(1, 255)]):
            msg = '模拟，正在检查 %s 上的漏洞。。。' % ip
            print(msg)
            if i % 5 == 0:
                self.my_signal.emit(msg +'[发现漏洞]')
            else:
                self.my_signal.emit('')
            time.sleep(0.01)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    app.exec()


