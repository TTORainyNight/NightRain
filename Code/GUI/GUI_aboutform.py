from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QThread

class GUI_aboutform(QWidget):
    # 加载父类
    def __init__(self):
        super().__init__()
        self.aboutform()

    def aboutform(self):
        from PyQt6.QtCore import Qt
        from Code.ui.UI_aboutform import Ui_aboutform
        from Code.lib.nrUpadte import Update
        # 设置关于窗口
        self.ui = Ui_aboutform()
        self.ui.setupUi(self)
        self.setWindowTitle("夜雨为伴-关于窗口")
        self.ui.logo_label.setStyleSheet("border-image: url(Source/image/logo_name.png);")
        self.ui.back_label.setStyleSheet("border-image: url(Source/image/xiaomeng.jpg);")
        with open(r"Source\text\about.txt", "r", encoding="utf-8") as file:
                about_information = file.read()
        self.ui.about_browser.setText(about_information)
        # 版本信息
        version_obj = Update(False)
        error, beta, inf = version_obj.get_version(r"Source\text\about.txt")
        if error:
            version = "None"
        else:
            self.version = inf
            if beta:
                version = "内测 " + str(inf)
            else:
                version = "V " + str(inf)
        self.ui.vision_label.setText(version)
        # 关于窗口信号槽
        self.ui.update_button.clicked.connect(self.update_button_clicked)
        
        # 修复右键菜单样式异常
        self.ui.about_browser.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.ui.about_browser.customContextMenuRequested.connect(self.about_browser_ContextMenu)
        
    # 关于信息右键修复
    def about_browser_ContextMenu(self, pos):
        from Code.GUI.GUI_control import nrControl_bjects
        nrControl_bjects().rewrite_browser_ContextMenu(
                    pos = pos, parent = self,
                    reobject = self.ui.about_browser)
        
    # 检查更新按钮
    def update_button_clicked(self):
        self.ui.update_label.setText("正在检查更新，请稍后……")
        # 设置子线程
        self.check_update_Thread = check_update_Thread()
        self.check_update_Thread.update_finish_sign.connect(self.update_show_result)
        # 调用子线程
        self.check_update_Thread.terminate()
        self.check_update_Thread.version = self.version
        self.check_update_Thread.start()

    # 展示获取更新的结果
    def update_show_result(self, reply):
        from json import loads
        reply = loads(reply)
        if reply["error"]:
            self.ui.update_label.setText("似乎断网了，请检查网络！")
        else:
            if reply["new_version"]:
                from Code.GUI.GUI_infoform import GUI_infoform
                self.ui.update_label.setText("已发现新版本，您可以下载更新！")
                update_info = "新版本：\n    " + reply["Version"] + "\n版本更新内容：\n  " + reply["Information"] + "\n下载地址：\n  " + reply["Url"] + "\n\n  您可以复制地址到浏览器进行下载" + "\n更新时间：\n  " + reply["Date"] + "\n更新包大小（不含资源）：\n  " + reply["Size"] + "\n其他信息:\n  " + reply["More"]
                updateform = GUI_infoform()
                updateform.ui.tip_label.setText("已发现全新版本，您可以下载更新！")
                updateform.ui.info_browser.append(update_info)
                updateform.exec()
            else:
                self.ui.update_label.setText("恭喜，已是最新版本！")

# “检查更新”按钮子线程  
class check_update_Thread(QThread):

    # 主线程通信信号，获取更新结束
    from PyQt6.QtCore import pyqtSignal
    update_finish_sign = pyqtSignal(str)

    def run(self):
        from Code.lib.nrUpadte import Update
        from json import dumps
        new_version = None
        up_json = {"error" : True}
        # 添加镜像站
        basic_url = "https://raw.githubusercontent.com/TTORainyNight/NightRain/main/update/update.json"
        urls = ["https://ghproxy.com/" + basic_url, basic_url, "https://gh.api.99988866.xyz/" + basic_url]
        obj = Update(False)
        error, up_json = obj.get_update(urls, 3)
        if error:
            new_version = obj.is_update(up_json, self.version)
            reply = up_json
            reply["error"] = False
        else:
            reply = {"error" : True}
        reply["new_version"] = new_version
        self.update_finish_sign.emit(dumps(reply))