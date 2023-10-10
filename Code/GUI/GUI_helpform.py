from PyQt6.QtWidgets import QWidget

class GUI_helpform(QWidget):
    # 加载父类
    def __init__(self):
        super().__init__()
        self.helpform()

    def helpform(self):
        from PyQt6.QtCore import Qt
        from Code.ui.UI_helpform import Ui_helpform
        # 设置对话窗口
        self.ui = Ui_helpform()
        self.ui.setupUi(self)
        self.setWindowTitle("夜雨为伴-帮助窗口")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng.jpg);")
        with open(r"Source\text\help.txt", "r", encoding="utf-8") as file:
                help_information = file.read()
        self.ui.help_browser.setText(help_information)
        # 修复右键菜单样式异常
        self.ui.help_browser.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.help_browser.customContextMenuRequested.connect(self.help_browser_ContextMenu)
    # 帮助信息右键修复
    def help_browser_ContextMenu(self, pos):
        from Code.GUI.GUI_control import nrControl_bjects
        nrControl_bjects().rewrite_browser_ContextMenu(
                    pos = pos, parent = self,
                    reobject = self.ui.help_browser)