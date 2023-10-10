from PyQt6.QtWidgets import QDialog

class GUI_setplusform(QDialog):
    # 加载父类
    # 要加载成QDialog啊，mainform和widget直接exec会报错，哎咦~~
    def __init__(self, plusInputData):
        super().__init__()
        self.ID = plusInputData
        self.setplusform()
        self.setplusform_load()

    def setplusform(self):
        from PyQt6.QtGui import QIcon
        from Code.ui.UI_setplusform import Ui_setplusform
        # 设置窗口
        self.ui = Ui_setplusform()
        self.ui.setupUi(self)
        # QDialog单独的logo
        self.setWindowIcon(QIcon("Source\image\logo.ico"))
        self.setWindowTitle("夜雨为伴-高级设置")
        self.ui.back_label.setStyleSheet("background-image: url(Source/image/xiaomeng.jpg);")
        self.ui.history_combobox.addItems(['开启', '关闭'])

        # 高级设置信号槽
        self.ui.save_Button.clicked.connect(self.save_Button_clicked)
        self.ui.unsave_Button.clicked.connect(self.unsave_Button_clicked)

    # 窗口加载
    def setplusform_load(self):
        self.ui.tempdir_lineedit.setText(self.ID["temp_dir"])
        self.ui.address_lineedit.setText(self.ID["address"])
        self.ui.temperature_lineedit.setText(str(self.ID["temperature"]))
        if self.ID["history"]:
            self.ui.history_combobox.setCurrentIndex(0)
        else:
            self.ui.history_combobox.setCurrentIndex(1)
        self.ui.indexrate_lineedit.setText(str(self.ID["indexrate"]))
        self.ui.filter_lineedit.setText(str(self.ID["filter_radius"]))
        self.ui.resample_lineedit.setText(str(self.ID["resample"]))
        self.ui.rmsmix_lineedit.setText(str(self.ID["rmsmix"]))
        self.ui.protect_lineedit.setText(str(self.ID["protect"]))

    # 保存返回按钮
    def save_Button_clicked(self):
        self.ID["temp_dir"] = self.ui.tempdir_lineedit.text()
        self.ID["address"] = self.ui.address_lineedit.text()
        self.ID["temperature"] = float(self.ui.temperature_lineedit.text())
        if self.ui.history_combobox.currentText() == "开启":
            self.ID["history"] = True
        elif self.ui.history_combobox.currentText() == "关闭":
            self.ID["history"] = False
        self.ID["indexrate"] = float(self.ui.indexrate_lineedit.text())
        self.ID["filter_radius"] = float(self.ui.filter_lineedit.text())
        self.ID["resample"] = int(self.ui.resample_lineedit.text())
        self.ID["rmsmix"] = float(self.ui.rmsmix_lineedit.text())
        self.ID["protect"] = float(self.ui.protect_lineedit.text())
        self.ID["save"] = True
        self.close()

    # 不保存返回按钮
    def unsave_Button_clicked(self):
        self.close()