from PyQt6.QtWidgets import QDialog

class GUI_infoform(QDialog):
    # 加载父类
    # 要加载成QDialog啊，mainform和widget直接exec会报错，哎咦~~
    def __init__(self):
        super().__init__()
        self.infoform()

    def infoform(self):
        from PyQt6.QtGui import QIcon
        from Code.ui.UI_infoform import Ui_infoform
        # 设置信息窗口，用于展示各类错误，大批量提示信息
        self.ui = Ui_infoform()
        self.ui.setupUi(self)
        # QDialog需要单独的logo
        self.setWindowIcon(QIcon("Source\image\logo.ico"))
        self.setWindowTitle("夜雨为伴-信息")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng_V.jpg);")
        # 信息窗口信号槽
        self.ui.OK_button.clicked.connect(self.OK_button_clicked)

    # 关闭按钮
    def OK_button_clicked(self):
        self.close()