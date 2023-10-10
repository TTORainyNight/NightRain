from PyQt6.QtWidgets import QDialog

class GUI_supportform(QDialog):
    # 加载父类
    # 要加载成QDialog啊，mainform和widget直接exec会报错，哎咦~~
    def __init__(self):
        super().__init__()
        self.supportform()

    def supportform(self):
        from PyQt6.QtGui import QIcon
        from Code.ui.UI_supportform import Ui_supportform
        # 设置赞助窗口
        self.ui = Ui_supportform()
        self.ui.setupUi(self)
        # QDialog需要单独的logo
        self.setWindowIcon(QIcon("Source\image\logo.ico"))
        self.setWindowTitle("夜雨为伴-赞助")
        self.ui.image_label.setStyleSheet("border-image: url(Source/image/supportQR.jpg);")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng_V.jpg);")