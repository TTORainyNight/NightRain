# 主程序启动入口
class NightRain():
    def __init__(self):
        from sys import argv
        from PyQt6.QtWidgets import QSplashScreen, QApplication
        from PyQt6.QtGui import QPixmap
        # 启动画面
        app = QApplication(argv)
        splash = QSplashScreen(QPixmap(r"Source\image\load.png"))
        splash.show()
        app.processEvents()
        # 启动程序
        from Code.GUI.GUI_mainform import GUI_mainform
        nrGUI = GUI_mainform()
        nrGUI.show()
        # 关闭启动画面
        splash.finish(nrGUI)
        app.exec()

# 调用信息窗口，展示错误信息
class Bug():
    def __init__(self):
        from sys import argv
        from PyQt6.QtWidgets import QApplication
        from Code.GUI.GUI_infoform import GUI_infoform
        # 读取
        with open(r"Temp\error.log", "r", encoding="utf-8") as file:
            error_info = file.read()
        #展示
        app = QApplication(argv)
        errorform = GUI_infoform()
        errorform.ui.tip_label.setText("很遗憾，应用程序出现了意外的错误。这对于夜雨为伴的改进十分重要，我希望您可以把它告诉我！\n以下是错误记录，请联系开发者：")
        errorform.ui.info_browser.append("程序错误信息，已写入日志Temp\error.log，详细信息：\n" + error_info)
        errorform.show()
        app.exec()