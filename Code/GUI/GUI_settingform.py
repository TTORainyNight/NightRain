from os.path import exists

from PyQt6.QtWidgets import QWidget, QMessageBox

from Code.GUI.GUI_control import nrControl_bjects
file_select = nrControl_bjects().file_select

class GUI_settingform(QWidget):

    # 加载父类
    def __init__(self):
        super().__init__()
        self.settingform()

    def settingform(self):
        from Code.ui.UI_settingform import Ui_settingform
        # 设置窗口
        self.ui = Ui_settingform()
        self.ui.setupUi(self)
        self.setWindowTitle("夜雨为伴-设置窗口")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng.jpg);")
        self.ui.ChatGPTmodel_combobox.addItems(['gpt-3.5-turbo', 'gpt-4'])
        self.ui.device_combobox.addItems(['GPU', 'CPU'])
        self.ui.method_combobox.addItems(['crepe', 'pm', 'harvest'])
        self.plusID = {'save' : False}
        self.newjson_button_clicked()

        # 设置窗口信号槽
        self.ui.newjson_button.clicked.connect(self.newjson_button_clicked)
        self.ui.loadjson_button.clicked.connect(self.loadjson_button_clicked)
        self.ui.savejson_button.clicked.connect(self.savejson_button_clicked)
        self.ui.checkequip_button.clicked.connect(self.checkequip_button_clicked)
        self.ui.cleartemp_button.clicked.connect(self.cleartemp_button_clicked)
        self.ui.setplus_button.clicked.connect(self.setplus_button_clicked)
        self.ui.select_json_button.clicked.connect(self.select_json_button_clicked)
        self.ui.select_userprompt_button.clicked.connect(self.select_userprompt_button_clicked)
        self.ui.select_pth_button.clicked.connect(self.select_pth_button_clicked)
        self.ui.select_index_button.clicked.connect(self.select_index_button_clicked)

    # 设置窗口槽函数
    # 新建配置文件
    def newjson_button_clicked(self):
        self.ui.jsonfile_lineedit.setText("")
        self.ui.name_lineedit.setText("")
        self.ui.ChatGPTmodel_combobox.setCurrentIndex(0)
        self.ui.userprompt_lineedit.setText("")
        self.ui.voicemodel_pth_lineedit.setText("")
        self.ui.voicemodel_index_lineedit.setText("")
        self.ui.device_combobox.setCurrentIndex(0)
        self.ui.upkey_lineedit.setText("0")
        self.ui.method_combobox.setCurrentIndex(0)
        self.plusID["temp_dir"] = "Temp"
        self.plusID["address"] = "https://api.openai.com"
        self.plusID["temperature"] = 1.0
        self.plusID["history"] = True
        self.plusID["indexrate"] = 0.75
        self.plusID["filter_radius"] = 3
        self.plusID["resample"] = 0
        self.plusID["rmsmix"] = 0.36
        self.plusID["protect"] = 0.33
        self.ui.output_browser.append("已新建设置文件 … …")

    # 打开配置文件
    def loadjson_button_clicked(self):
        from Code.lib.nrData import user_data as uds
        file = self.ui.jsonfile_lineedit.text()
        if exists(file):
            ud = uds().read(file)
            self.ui.name_lineedit.setText(ud["VHumanName"])
            self.ui.ChatGPTmodel_combobox.setCurrentText(ud["ChatModel"])
            self.ui.userprompt_lineedit.setText(ud["UserPromptFile"])
            self.ui.voicemodel_pth_lineedit.setText(ud["VoiceModel_pth"])
            self.ui.voicemodel_index_lineedit.setText(ud["VoiceModel_index"])
            self.ui.device_combobox.setCurrentText(ud["Device"])
            self.ui.method_combobox.setCurrentText(ud["Method"])
            self.ui.upkey_lineedit.setText(str(ud["Upkey"]))
            self.plusID["temp_dir"] = ud["TempDir"]
            self.plusID["address"] = ud["Address"]
            self.plusID["temperature"] = ud["Temperature"]
            self.plusID["history"] = ud["History"]
            self.plusID["indexrate"] = ud["IndexRate"]
            self.plusID["filter_radius"] = ud["Filter"]
            self.plusID["resample"] = ud["Resample"]
            self.plusID["rmsmix"] = ud["Rmsmix"]
            self.plusID["protect"] = ud["Protect"]
            self.ui.output_browser.append("加载设置文件完毕 … …")
            self.ui.output_browser.append("修改后记得保存哦！")
            QMessageBox.information(self,"注啦意！","更多更牛13的设置，请点击“高级设置”")
        else:
            self.ui.output_browser.append("配置文件不存在，请检查")

    # 保存配置文件
    def savejson_button_clicked(self):
        from Code.lib.nrData import user_data as uds
        # 获取当前数据
        file = self.ui.jsonfile_lineedit.text()
        name = self.ui.name_lineedit.text()
        prompt = self.ui.userprompt_lineedit.text()
        tempdir = self.plusID["temp_dir"]
        voicemodel_pth = self.ui.voicemodel_pth_lineedit.text()
        voicemodel_index = self.ui.voicemodel_index_lineedit.text()
        device = self.ui.device_combobox.currentText()
        method = self.ui.method_combobox.currentText()
        upkey = int(self.ui.upkey_lineedit.text())
        address = self.plusID["address"]
        temperature = self.plusID["temperature"]
        indexrate = float(self.plusID["indexrate"])
        filter_radius = float(self.plusID["filter_radius"])
        resample = int(self.plusID["resample"])
        rmsmix = float(self.plusID["rmsmix"])
        protect = float(self.plusID["protect"])

        # 检查数据
        allow_write = True
        error_list, rewrite_list = uds().check(
              file, name, tempdir, voicemodel_pth, voicemodel_index, 
              prompt, device, method, upkey, temperature, address, 
              indexrate, filter_radius, resample, rmsmix, protect)
        if error_list:
            allow_write = False
            for key, value in error_list.items():
                self.ui.output_browser.append(value)
        else:
            prompt = rewrite_list.get('prompt', prompt)
            voicemodel_pth = rewrite_list.get('voicemodel_pth', voicemodel_pth)
            voicemodel_index = rewrite_list.get('voicemodel_index', voicemodel_index)

        # 写入数据
        if allow_write:
            reply = 16384
            if exists(file):
                reply = QMessageBox.question(self,"注啦意！","配置文件已存在，要更新吗？\n确定？")
            if reply == 16384:
                ud = {}
                ud["VHumanName"] = name
                ud["ChatModel"] = self.ui.ChatGPTmodel_combobox.currentText()
                ud["Address"] = address
                ud["Temperature"] = temperature
                ud["History"] = self.plusID["history"]
                ud["UserPromptFile"] = prompt
                ud["TempDir"] = tempdir
                ud["VoiceModel_pth"] = voicemodel_pth
                ud["VoiceModel_index"] = voicemodel_index
                ud["Device"] = device
                ud["Method"] = method
                ud["Upkey"] = upkey
                ud["IndexRate"] = indexrate
                ud["Filter"] = filter_radius
                ud["Resample"] = resample 
                ud["Rmsmix"] = rmsmix
                ud["Protect"] = protect
                uds().save(ud, file)
                self.ui.output_browser.append(f"成功保存到{file}")
            else:
                self.ui.output_browser.append("什么也没干… …")

    # 清空缓存
    def cleartemp_button_clicked(self):
        from os import listdir
        from os import remove
        from os.path import abspath
        from os.path import join
        reply = QMessageBox.question(self,"注啦意！","即将删除掉缓存目录下全部文件，世上没有后悔药！\n确定？")
        if reply == 16384:
            tempdir = abspath(self.plusID["temp_dir"])
            if exists(tempdir):
                for filename in listdir(tempdir):
                    file_path = join(tempdir, filename)
                    remove(file_path)
                if listdir(tempdir) == []:
                    self.ui.output_browser.append("缓存清理干净了呢 … …")
                else:
                    self.ui.output_browser.append("清空失败，请再次尝试 … …")
            else:
                self.ui.output_browser.append("清空失败，缓存目录不存在，请指定一个缓存目录")
        else:
            self.ui.output_browser.append("什么也没有干 … …")

    # 检测设备
    def checkequip_button_clicked(self):
        from torch import cuda
        if cuda.is_available():
            self.ui.output_browser.append("恭喜，您的GPU可用：\n" + str(cuda.get_device_name(0)))
        else:
            self.ui.output_browser.append("很遗憾，未检测到您的GPU… …\n  检查GPU，CUDA，cuDNN")

    # 高级设置
    def setplus_button_clicked(self):
        from Code.GUI.GUI_setplusform import GUI_setplusform as plus
        QMessageBox.information(self,"注啦意！","高级设置可以更精准的调试AI模型，不过呢，除非出现错误，一般不建议调整")
        self.plusID['save'] = False
        plusform = plus(self.plusID)
        plusform.exec()
        self.plusID = plusform.ID
        if self.plusID["save"] == True:
            self.ui.output_browser.append("高级设置已保存")
        elif self.plusID["save"] == False:
            self.ui.output_browser.append("高级设置未保存 … …")
            
    # 一堆文件选择按钮
    def select_json_button_clicked(self):
        reply = file_select(self, tips = "虚拟人配置", extension = "JSON Files (*.json)")
        if reply:
            self.ui.jsonfile_lineedit.setText(reply)
    def select_userprompt_button_clicked(self):
        reply = file_select(self, tips = "角色设定", extension = "TEXT Files (*.txt)")
        if reply:
            self.ui.userprompt_lineedit.setText(reply)
    def select_pth_button_clicked(self):
        reply = file_select(self, tips = "声音模型", extension = "PTH Files (*.pth)")
        if reply:
            self.ui.voicemodel_pth_lineedit.setText(reply)
    def select_index_button_clicked(self):
        reply = file_select(self, tips = "声音模型", extension = "INDEX Files (*.index)")
        if reply:
            self.ui.voicemodel_index_lineedit.setText(reply)