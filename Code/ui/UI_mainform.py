# Form implementation generated from reading ui file 'mainform.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_mainform(object):
    def setupUi(self, mainform):
        mainform.setObjectName("mainform")
        mainform.resize(1180, 720)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        mainform.setFont(font)
        self.talk_button = QtWidgets.QPushButton(parent=mainform)
        self.talk_button.setGeometry(QtCore.QRect(40, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.talk_button.setFont(font)
        self.talk_button.setObjectName("talk_button")
        self.dock_line1 = QtWidgets.QFrame(parent=mainform)
        self.dock_line1.setGeometry(QtCore.QRect(170, 30, 3, 61))
        self.dock_line1.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dock_line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dock_line1.setObjectName("dock_line1")
        self.dock_line2 = QtWidgets.QFrame(parent=mainform)
        self.dock_line2.setGeometry(QtCore.QRect(330, 30, 3, 61))
        self.dock_line2.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dock_line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dock_line2.setObjectName("dock_line2")
        self.sing_button = QtWidgets.QPushButton(parent=mainform)
        self.sing_button.setGeometry(QtCore.QRect(210, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.sing_button.setFont(font)
        self.sing_button.setObjectName("sing_button")
        self.dock_line3 = QtWidgets.QFrame(parent=mainform)
        self.dock_line3.setGeometry(QtCore.QRect(500, 30, 3, 61))
        self.dock_line3.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dock_line3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dock_line3.setObjectName("dock_line3")
        self.person_button = QtWidgets.QPushButton(parent=mainform)
        self.person_button.setGeometry(QtCore.QRect(370, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.person_button.setFont(font)
        self.person_button.setObjectName("person_button")
        self.dock_line4 = QtWidgets.QFrame(parent=mainform)
        self.dock_line4.setGeometry(QtCore.QRect(657, 30, 3, 61))
        self.dock_line4.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dock_line4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dock_line4.setObjectName("dock_line4")
        self.setting_button = QtWidgets.QPushButton(parent=mainform)
        self.setting_button.setGeometry(QtCore.QRect(530, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.setting_button.setFont(font)
        self.setting_button.setObjectName("setting_button")
        self.dock_line5 = QtWidgets.QFrame(parent=mainform)
        self.dock_line5.setGeometry(QtCore.QRect(820, 30, 3, 61))
        self.dock_line5.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.dock_line5.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.dock_line5.setObjectName("dock_line5")
        self.help_button = QtWidgets.QPushButton(parent=mainform)
        self.help_button.setGeometry(QtCore.QRect(690, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.help_button.setFont(font)
        self.help_button.setObjectName("help_button")
        self.about_button = QtWidgets.QPushButton(parent=mainform)
        self.about_button.setGeometry(QtCore.QRect(850, 30, 91, 61))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        self.about_button.setFont(font)
        self.about_button.setObjectName("about_button")
        self.mainform_line1 = QtWidgets.QFrame(parent=mainform)
        self.mainform_line1.setGeometry(QtCore.QRect(70, 100, 1041, 16))
        self.mainform_line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.mainform_line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.mainform_line1.setObjectName("mainform_line1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=mainform)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 680, 1161, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.statusbar_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.statusbar_layout.setContentsMargins(0, 0, 0, 0)
        self.statusbar_layout.setObjectName("statusbar_layout")
        self.agreement_checkbox = QtWidgets.QCheckBox(parent=self.horizontalLayoutWidget)
        self.agreement_checkbox.setChecked(True)
        self.agreement_checkbox.setObjectName("agreement_checkbox")
        self.statusbar_layout.addWidget(self.agreement_checkbox)
        self.RainyFriend_agreement_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setUnderline(True)
        self.RainyFriend_agreement_button.setFont(font)
        self.RainyFriend_agreement_button.setObjectName("RainyFriend_agreement_button")
        self.statusbar_layout.addWidget(self.RainyFriend_agreement_button)
        self.Apache_agreement_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(11)
        font.setUnderline(True)
        self.Apache_agreement_button.setFont(font)
        self.Apache_agreement_button.setObjectName("Apache_agreement_button")
        self.statusbar_layout.addWidget(self.Apache_agreement_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.statusbar_layout.addItem(spacerItem)
        self.encourage_button = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("隶书")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.encourage_button.setFont(font)
        self.encourage_button.setObjectName("encourage_button")
        self.statusbar_layout.addWidget(self.encourage_button)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.statusbar_layout.addItem(spacerItem1)
        self.statusbar_layout.setStretch(3, 4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=mainform)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(25, 122, 1121, 531))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.show_layout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.show_layout.setContentsMargins(0, 0, 0, 0)
        self.show_layout.setObjectName("show_layout")
        self.mainform_line2 = QtWidgets.QFrame(parent=mainform)
        self.mainform_line2.setGeometry(QtCore.QRect(30, 660, 1101, 16))
        self.mainform_line2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.mainform_line2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.mainform_line2.setObjectName("mainform_line2")
        self.Test_label = QtWidgets.QLabel(parent=mainform)
        self.Test_label.setGeometry(QtCore.QRect(950, 30, 201, 61))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.Test_label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(22)
        font.setBold(True)
        font.setItalic(False)
        self.Test_label.setFont(font)
        self.Test_label.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.Test_label.setObjectName("Test_label")
        self.back_label = QtWidgets.QLabel(parent=mainform)
        self.back_label.setGeometry(QtCore.QRect(0, 0, 1180, 720))
        self.back_label.setStyleSheet("border-image: url(:/image/image/mainback.jpg);")
        self.back_label.setText("")
        self.back_label.setObjectName("back_label")
        self.back_label2 = QtWidgets.QLabel(parent=mainform)
        self.back_label2.setGeometry(QtCore.QRect(0, 0, 1180, 720))
        self.back_label2.setStyleSheet("background-color: rgba(255, 255, 255, 215);")
        self.back_label2.setText("")
        self.back_label2.setObjectName("back_label2")
        self.back_label.raise_()
        self.back_label2.raise_()
        self.talk_button.raise_()
        self.dock_line1.raise_()
        self.dock_line2.raise_()
        self.sing_button.raise_()
        self.dock_line3.raise_()
        self.person_button.raise_()
        self.dock_line4.raise_()
        self.setting_button.raise_()
        self.dock_line5.raise_()
        self.help_button.raise_()
        self.about_button.raise_()
        self.mainform_line1.raise_()
        self.horizontalLayoutWidget.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.mainform_line2.raise_()
        self.Test_label.raise_()

        self.retranslateUi(mainform)
        QtCore.QMetaObject.connectSlotsByName(mainform)

    def retranslateUi(self, mainform):
        _translate = QtCore.QCoreApplication.translate
        mainform.setWindowTitle(_translate("mainform", "Form"))
        self.talk_button.setText(_translate("mainform", "对话"))
        self.sing_button.setText(_translate("mainform", "歌曲"))
        self.person_button.setText(_translate("mainform", "形象"))
        self.setting_button.setText(_translate("mainform", "设置"))
        self.help_button.setText(_translate("mainform", "帮助"))
        self.about_button.setText(_translate("mainform", "关于"))
        self.agreement_checkbox.setText(_translate("mainform", "我已阅读并同意："))
        self.RainyFriend_agreement_button.setText(_translate("mainform", "《夜雨为伴用户使用协议》"))
        self.Apache_agreement_button.setText(_translate("mainform", "《Apache2.0开源协议》"))
        self.encourage_button.setText(_translate("mainform", "赞助"))
        self.Test_label.setText(_translate("mainform", "内测版本beta1"))
