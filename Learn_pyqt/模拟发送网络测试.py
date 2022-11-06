import sys
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Mywindow(QWidget):
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(500, 200)
        container = QVBoxLayout()

        self.msg = QLabel('')
        self.msg.resize(440, 15)
        print(self.msg.frameSize())
        self.msg.setWordWrap(True)  #自动换行
        self.msg.setAlignment(Qt.AlignTop)
        # self.msg.setStyleSheet('background-color:yellow; color: black;')

        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        h_layout = QHBoxLayout()
        btn = QPushButton('开始检查', self)
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        container.addLayout(v_layout)
        container.addLayout(h_layout)

        self.setLayout(container)

        self.my_signal.connect(self.my_solt)

    def my_solt(self, msg):
        print(msg)
        self.msg_history.append(msg)
        self.msg.setText('<br>'.join(self.msg_history))
        self.msg.resize(400, self.msg.frameSize().height() + 15)
        self.msg.repaint() #更新内容

    def check(self):
        for i, ip in enumerate(['192.168.1.%d' % x for x in range(1, 255)]):
            msg = '模拟，正在检查%s 上的漏洞' % ip
            if i % 5 == 0:
                self.my_signal.emit(msg + '[发现漏洞]')
            time.sleep(0.1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    app.exec()