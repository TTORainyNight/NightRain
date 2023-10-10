from PyQt6.QtWidgets import QWidget

class GUI_talkform(QWidget):
    # 加载父类
    def __init__(self):
        super().__init__()
        self.talkform()

    def talkform(self):
        from Code.ui.UI_talkform import Ui_talkform
        # 设置对话窗口
        self.ui = Ui_talkform()
        self.ui.setupUi(self)
        self.setWindowTitle("夜雨为伴-对话窗口")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng.jpg);")
        self.ui.talkoutput_browser.setText("正在等待启动 … …")
        self.ui.ChatGPToutput_browser.setText("AI：你好，我是你的虚拟人小助手！")

        # 对话窗口信号槽
        self.ui.talkstart_button.clicked.connect(self.talkstart_button_clicked)
        self.ui.ChatGPTinput_button.clicked.connect(self.ChatGPTinput_button_clicked)
        self.ui.ChatGPTvoice_button.clicked.connect(self.ChatGPTvoice_button_clicked)
        self.ui.ChatGPTnew_button.clicked.connect(self.ChatGPTnew_button_clicked)
        self.ui.select_json_button.clicked.connect(self.select_json_button_clicked)

    # 对话窗口槽函数
    # “启动”按钮
    def talkstart_button_clicked(self):
        from os.path import exists
        from Code.lib.con_talkform import talkstart_Thread
        # 设置子线程
        self.talkstart_Thread = talkstart_Thread()
        self.talkstart_Thread.talkstart_finish_sign.connect(self.talkstart_successful)
        # 获取API_key，读取用户配置，处理用户配置
        api_key = self.ui.API_Key_lineedit.text()
        json_file = self.ui.setting_lineedit.text()
        # 检测json配置文件是否存在
        if exists(json_file):
            self.ui.talkoutput_browser.append("正在加载AI模型 … …")
            self.ui.talkstart_button.setEnabled(False)
            self.ui.talkstart_button.setText("正在启动……")

            # 加载虚拟人照片，此部分后续会删除 to do
            # 需要更改为人物建模加载
            from pathlib import Path
            image_path = (str(Path(json_file).parent) + "\\vhuman.jpg").replace('\\', '/')
            if exists(image_path):
                self.ui.imagelabel.setStyleSheet(f"border-image: url({image_path});")

            # 启动子线程
            self.talkstart_Thread.terminate()
            self.talkstart_Thread.api_key = api_key
            self.talkstart_Thread.json_file = json_file
            self.talkstart_Thread.start()
        else:
            self.ui.talkoutput_browser.append("配置文件好像不太对啊 … …")
        
    # “发送”按钮
    def ChatGPTinput_button_clicked(self):
        from Code.lib.con_talkform import ChatGPTInput_Thread
        # 设置子线程
        self.ChatGPTinput_Thread = ChatGPTInput_Thread()
        self.ChatGPTinput_Thread.chat_text_finish_sign.connect(self.ChatGPT_show_result)
        if not(self.userdata["MaxToken"]):
            self.ui.ChatGPTinput_button.setEnabled(False)
            self.ui.ChatGPTvoice_button.setEnabled(False)
            # 内容读取
            self.userdata["Input"] = self.ui.ChatGPTinput_textedit.toPlainText()
            # 添加显示
            self.ui.ChatGPTinput_textedit.setText("")
            self.ui.ChatGPToutput_browser.append("你：" + self.userdata["Input"])
            self.ui.ChatGPToutput_browser.verticalScrollBar().setValue(self.ui.ChatGPToutput_browser.verticalScrollBar().maximum())
            self.ui.talkoutput_browser.append(self.userdata["VHumanName"] + "正在思考 … …")
            self.ui.talkoutput_browser.verticalScrollBar().setValue(self.ui.talkoutput_browser.verticalScrollBar().maximum())
            # 调用子线程
            self.ChatGPTinput_Thread.terminate()
            self.ChatGPTinput_Thread.option = "chat_text"
            self.ChatGPTinput_Thread.userdata = self.userdata
            self.ChatGPTinput_Thread.start()
        else:
            self.ui.talkoutput_browser.append("本次对话达到上限，请开启新对话以继续！")
            self.ui.talkoutput_browser.verticalScrollBar().setValue(self.ui.talkoutput_browser.verticalScrollBar().maximum())

    # “语音”按钮
    def ChatGPTvoice_button_clicked(self):
        self.ui.talkoutput_browser.append("莫急，此功能开发中  to do")
        self.ui.talkoutput_browser.verticalScrollBar().setValue(self.ui.talkoutput_browser.verticalScrollBar().maximum())
        pass #to do

    # “新对话”按钮
    def ChatGPTnew_button_clicked(self):
        from PyQt6.QtWidgets import QMessageBox
        from Code.lib.con_talkform import con_talkform as co
        reply = QMessageBox.question(self,"注啦意！","即将新建对话，这会清空之前的全部历史哦！\n确定？")
        if reply == 16384:
            reply = co().ChatGPTnew(self.userdata["History_File"], self.userdata["Error_File"], self.userdata["TempDir"])
            if reply:
                self.ui.talkoutput_browser.setText("焕然一新，很乐意重新开始！")
                self.ui.ChatGPToutput_browser.setText("好呀，我很乐意重新开始！")
                self.userdata["MaxToken"] = False
            else:
                self.ui.talkoutput_browser.append("新对话失败！请再次尝试！")
        else:
            self.ui.talkoutput_browser.append("什么也没干 … …")
    
    # 展示ChatGPT文本
    def ChatGPT_show_result(self, reply):
        from json import loads
        reply = loads(reply)
        maxtoken = reply["maxtoken"]
        reply = reply["reply"]
        # 显示内容
        self.ui.ChatGPToutput_browser.append(self.userdata["VHumanName"] + "：" + reply + "\n")
        self.ui.ChatGPToutput_browser.verticalScrollBar().setValue(self.ui.ChatGPToutput_browser.verticalScrollBar().maximum())
        # 重开开启发送语音按钮
        self.ui.ChatGPTinput_button.setEnabled(True)
        self.ui.ChatGPTvoice_button.setEnabled(True)
        # 设定历史
        self.userdata["MaxToken"] = maxtoken

        # 重启子线程，文字转语音
        self.ChatGPTinput_Thread.terminate()
        self.ChatGPTinput_Thread.option = "chat_tovoice"
        self.ChatGPTinput_Thread.reply = reply
        self.ChatGPTinput_Thread.userdata = self.userdata
        self.ChatGPTinput_Thread.start()

    # 启动成功
    def talkstart_successful(self, reply):
        from os.path import exists
        # 展示相关内容
        if reply:
            self.userdata = self.talkstart_Thread.userdata
            self.talkstart_Thread.terminate()
            self.ui.tips_label.setText(self.userdata["VHumanName"] + "\n\n夜雨为伴\nNightRain Companion")
            self.ui.talkoutput_browser.append("让我找找历史对话在不在 … …")
            history_file = self.userdata["History_File"]
            history = ""
            if exists(history_file):
                with open(history_file, 'r', encoding="utf-8") as file:
                    history = file.read()
                self.ui.ChatGPToutput_browser.setText(history + "\n-----以上是历史对话-----\n")
                self.ui.ChatGPToutput_browser.verticalScrollBar().setValue(self.ui.ChatGPToutput_browser.verticalScrollBar().maximum())
            else:
                self.ui.ChatGPToutput_browser.setText("没有找到读取到历史对话^-^\n")
            self.ui.talkstart_button.setEnabled(False)
            self.ui.ChatGPTinput_button.setEnabled(True)
            self.ui.ChatGPTvoice_button.setEnabled(True)
            self.ui.ChatGPTnew_button.setEnabled(True)
            self.ui.talkstart_button.hide()
            self.ui.select_json_button.hide()
            self.ui.talkoutput_browser.append("启动成功啦！快去聊天吧！")
        else:
            self.ui.talkoutput_browser.append("失败啦！\n  配置文件错误，请在“设置”中重新保存 … …")
            self.ui.talkstart_button.setEnabled(True)
            self.ui.talkstart_button.setText("启动")
    # 选择配置文件按钮
    def select_json_button_clicked(self):
        from Code.GUI.GUI_control import nrControl_bjects
        reply = nrControl_bjects().file_select(self, tips = "虚拟人配置", extension = "JSON Files (*.json)")
        if reply:
            self.ui.setting_lineedit.setText(reply)