from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QColor
import sys
import pyperclip

# pyinstaller -F -w -i D:\workspace_py\GomokuCode\tools\app.ico color_picker.py

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.color = object
        self.colText = QLabel(self)
        self.colStatus = QLabel(self)
        self.width = 300
        self.height = 200

    def setup_ui(self):
        self.setWindowTitle("取色器")
        self.resize(self.width, self.height)
        self.move(500, 300)

        # 颜色值显示
        self.colText.setText("颜色值: #000000")
        self.colText.resize(self.width, 50)
        self.colText.move(0, 30)
        self.colText.setAlignment(Qt.AlignHCenter)
        # 取色状态指示
        self.colStatus.setText("tips")
        self.colStatus.resize(self.width, 50)
        self.colStatus.move(0, 150)
        self.colStatus.setAlignment(Qt.AlignHCenter)

        btn_select = QPushButton(self)
        btn_select.setText("取色")
        btn_select.move(50, 80)
        btn_select.resize(75,30)
        btn_select.clicked.connect(lambda: self.pick_color())

        btn_copy = QPushButton(self)
        btn_copy.setText("复制")
        btn_copy.move(175, 80)
        btn_copy.resize(75,30)
        btn_copy.clicked.connect(lambda: self.copy_color(self.color))

    def pick_color(self):
        self.color = QColorDialog.getColor()
        self.colText.setText("颜色值: " + self.color.name())
        self.colStatus.setText("tips")

    def copy_color(self, color):
        if type(color) is QColor:
            pyperclip.copy(color.name())
            self.colStatus.setText("复制成功")
            print("复制成功")
        else:
            print("请先取色")
            self.colStatus.setText("请先取色")

    def show1(self):
        self.setup_ui()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    # win.setup_ui()
    win.show1()
    sys.exit(app.exec_())
