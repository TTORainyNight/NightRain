# 此处存放对于GUI复用性高的代码

class nrControl_bjects():
    
    # 选择文件，传入参数为两个提示信息的字符串
    # 有文件返回路径，无文件返回False
    def file_select(self, parent, tips = "选择文件", extension = "JSON Files (*.json)"):
        from PyQt6.QtWidgets import QFileDialog
        file_dir, _ = QFileDialog.getOpenFileName(parent, tips, "", extension)
        if file_dir:
            return file_dir
        return False
    
    # Qbrowser右键菜单修复
    # 传入参数为，槽函数提前设置的pos，父类，修复Qbrowser目标
    def rewrite_browser_ContextMenu(self, pos, parent, reobject):
        from PyQt6.QtGui import QAction
        menu = reobject.createStandardContextMenu(pos)
        menu.clear()
        copy_action = QAction("复制", parent)
        copy_action.triggered.connect(reobject.copy)
        menu.addAction(copy_action)
        select_action = QAction("选择全部", parent)
        select_action.triggered.connect(reobject.selectAll)
        menu.addAction(select_action)
        # QSS字符串
        menu.setStyleSheet("""
            QMenu {
                border: none;
                background-color: #fff;
                color: #000;
                padding: 0;
            }
            QMenu::item:selected {
                background-color: #ccc;
                color: #000;
            }   """)
        menu.exec(reobject.mapToGlobal(pos))