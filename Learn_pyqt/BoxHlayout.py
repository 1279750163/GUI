import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QRadioButton

class Mywindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        container = QVBoxLayout()

        hobby_box = QGroupBox('爱好')
        v_layout = QVBoxLayout()

        btn1 = QRadioButton('打游戏')
        btn2 = QRadioButton('看电影')
        btn3 = QRadioButton('看书')

        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)

        hobby_box.setLayout(v_layout)

        gender_box = QGroupBox('性别')
        h_layout = QHBoxLayout()

        btn4 = QRadioButton('男')
        btn5 = QRadioButton('女')

        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)

        gender_box.setLayout(h_layout)

        container.addWidget(hobby_box)
        container.addWidget(gender_box)
        self.setLayout(container)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Mywindow()
    w.show()
    app.exec()