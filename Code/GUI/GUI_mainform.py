from PyQt6.QtWidgets import QWidget

# 主窗口
class GUI_mainform(QWidget):
    # 加载父类，启动主窗口
    def __init__(self):
        super().__init__()
        self.mainform()

    def mainform(self):
        from PyQt6.QtGui import QIcon
        from Code.ui.UI_mainform import Ui_mainform
        from Code.GUI.GUI_talkform import GUI_talkform
        from Code.lib.nrUpadte import Update
        # 设置主窗口
        self.ui = Ui_mainform()
        self.ui.setupUi(self)
        self.setWindowTitle("夜雨为伴 NightRain Companion")
        self.setWindowIcon(QIcon("Source\image\logo.ico"))
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/mainback.jpg);")
        # 内测版本信息
        version_obj = Update(False)
        error, beta, inf = version_obj.get_version(r"Source\text\about.txt")
        if error:
            version = "程序错误"
        else:
            version = str(inf)
            if beta:
                version = "内测版本" + version
                self.ui.Test_label.setText(version)
            else:
                self.ui.Test_label.hide()
        # 添加子窗口，默认显示对话talk_form
        self.ui.show_layout.addWidget(GUI_talkform())
        # 这里注释掉的代码，用于调试的时候迅速启动相应界面
        # 可以放心删除，不影响功能
        #self.ui.show_layout.addWidget(GUI_settingform())

        # 主窗口信号槽
        self.ui.talk_button.clicked.connect(self.talk_button_clicked)
        self.ui.sing_button.clicked.connect(self.sing_button_clicked)
        self.ui.person_button.clicked.connect(self.person_button_clicked)
        self.ui.setting_button.clicked.connect(self.setting_button_clicked)
        self.ui.help_button.clicked.connect(self.help_button_clicked)
        self.ui.about_button.clicked.connect(self.about_button_clicked)
        self.ui.agreement_checkbox.stateChanged.connect(self.agreement_checkbox_stateChanged)
        self.ui.RainyFriend_agreement_button.clicked.connect(self.RainyFriend_agreement_button_clicked)
        self.ui.Apache_agreement_button.clicked.connect(self.Apache_agreement_button_clicked)
        self.ui.encourage_button.clicked.connect(self.encourage_button_clicked)
        
    # 主窗口槽函数
    # “对话”按钮
    def talk_button_clicked(self):
        from Code.GUI.GUI_talkform import GUI_talkform
        # 清空布局器中的全部窗口
        while self.ui.show_layout.count() > 0:
            item = self.ui.show_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()
        # 添加要展示的窗口
        self.ui.show_layout.addWidget(GUI_talkform())

    # “歌曲”按钮
    def sing_button_clicked(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "君，莫急", "该功能火速开发中，可能在新版本上线，敬请期待！\n to do")
        print("歌曲")
        pass #to do

    # “形象”按钮
    def person_button_clicked(self):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.information(self, "君，莫急", "该功能火速开发中，可能在新版本上线，敬请期待！\n to do")
        print("形象")
        pass #to do

    # “设置”按钮
    def setting_button_clicked(self):
        from Code.GUI.GUI_settingform import GUI_settingform
        while self.ui.show_layout.count() > 0:
            item = self.ui.show_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()
        # 添加要展示的窗口
        self.ui.show_layout.addWidget(GUI_settingform())

    # “帮助”按钮
    def help_button_clicked(self):
        from Code.GUI.GUI_helpform import GUI_helpform
        # 清空布局器中的全部窗口
        while self.ui.show_layout.count() > 0:
            item = self.ui.show_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()
        # 添加要展示的窗口
        self.ui.show_layout.addWidget(GUI_helpform())

    # “关于”按钮
    def about_button_clicked(self):
        from Code.GUI.GUI_aboutform import GUI_aboutform
        # 清空布局器中的全部窗口
        while self.ui.show_layout.count() > 0:
            item = self.ui.show_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.hide()
        # 添加要展示的窗口
        self.ui.show_layout.addWidget(GUI_aboutform())

    # “我已阅读…”状态改变
    def agreement_checkbox_stateChanged(self):
        from sys import exit
        from PyQt6.QtWidgets import QMessageBox
        # 用户拒绝协议，退出程序
        reply = QMessageBox.question(self,"您拒绝了使用协议","请认真阅读相关协议，若您不同意，本程序无法提供任何服务。即将退出！\n\n--拒绝相关协议并退出？")
        if reply == 16384:
            exit()
        else:   
            QMessageBox.information(self, "提示", "为了保护你我合法权益，请认真阅读相关协议，感谢配合！")
            self.ui.agreement_checkbox.setChecked(True)

    # “夜雨为伴用户协议”按钮
    def RainyFriend_agreement_button_clicked(self):
        from os import system
        system(r"start Source\text\夜雨为伴用户使用协议.txt")

    # “Apache开源协议”按钮
    def Apache_agreement_button_clicked(self):
        from os import system
        system(r"start Source\text\ApacheLicense2.0.txt")

    # “赞助”按钮
    def encourage_button_clicked(self):
        from Code.GUI.GUI_supportform import GUI_supportform
        GUI_supportform().exec()