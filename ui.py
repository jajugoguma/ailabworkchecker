# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 630)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 341, 631))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(2, 0, 331, 51))
        font = QtGui.QFont()
        font.setFamily("배달의민족 을지로체")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(105, 51, 221, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(8, 91, 171, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(190, 90, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(5, 150, 321, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_refresh = QtWidgets.QPushButton(self.tab)
        self.pushButton_refresh.setGeometry(QtCore.QRect(265, 90, 61, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 50, 101, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 160, 101, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.textEdit_workHour = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_workHour.setGeometry(QtCore.QRect(10, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit_workHour.setFont(font)
        self.textEdit_workHour.setObjectName("textEdit_workHour")
        self.textEdit_workMin = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_workMin.setGeometry(QtCore.QRect(130, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit_workMin.setFont(font)
        self.textEdit_workMin.setObjectName("textEdit_workMin")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(85, 285, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(207, 285, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_workTime = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_workTime.setGeometry(QtCore.QRect(250, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_workTime.setFont(font)
        self.pushButton_workTime.setObjectName("pushButton_workTime")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "AILab 출근 기록기"))
        self.label_2.setText(_translate("Dialog", "현재시간"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "출근"))
        self.pushButton_refresh.setText(_translate("Dialog", "새로\n"
"고침"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "출근"))
        self.label_4.setText(_translate("Dialog", "인원 추가"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'맑은 고딕\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; vertical-align:middle;\">이름 입력</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "추가"))
        self.pushButton_3.setText(_translate("Dialog", "삭제"))
        self.label_5.setText(_translate("Dialog", "인원 삭제"))
        self.textEdit_2.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'맑은 고딕\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; vertical-align:middle;\">이름 입력</span></p></body></html>"))
        self.label_6.setText(_translate("Dialog", "출근 시간"))
        self.label_7.setText(_translate("Dialog", "시"))
        self.label_8.setText(_translate("Dialog", "분"))
        self.pushButton_workTime.setText(_translate("Dialog", "변경"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "인원변동"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
