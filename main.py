import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.cron import CronTrigger
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import *
import telegram
import calendar


class TelBot:
    def __init__(self):
        self.telgm_token = 'token'
        self.bot = telegram.Bot(token=self.telgm_token)
        self.chatId = 'id'
        self.updates = self.bot.getUpdates()
        self.msgs = len(self.updates)

    def sendMsg(self, chatId, msg):
        self.bot.sendMessage(chat_id=chatId, text=msg)


class Time:
    def __init__(self):
        self.datetime = QDateTime.currentDateTime()
        self.YEAR = int(self.datetime.toString('yyyy'))
        self.MONTH = int(self.datetime.toString('MM'))
        self.DAY = int(self.datetime.toString('dd'))

    def getDate(self):
        self.datetime = QDateTime.currentDateTime()
        self.YEAR = int(self.datetime.toString('yyyy'))
        self.MONTH = int(self.datetime.toString('MM'))
        self.DAY = int(self.datetime.toString('dd'))


class GDrive:
    def __init__(self):
        self.spreadsheet_url = 'url'
        self.scope = [
            'https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
        ]
        self. dict = {
            "type": "service_account",
            "project_id": "worktime-265901",
            "private_key_id": "key",
            "private_key": "-----BEGIN PRIVATE KEY-----\nkey",
            "client_email": "mail",
            "client_id": "id",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "url"
        }
        self.credentials = ServiceAccountCredentials.from_json_keyfile_dict(self.dict, self.scope)
        self.gc = gspread.authorize(self.credentials)
        self.wb = self.gc.open_by_url(self.spreadsheet_url)
        self.actSheet = self.wb.worksheet(str(time.MONTH) + '월')
        self.memberSheet = self.wb.worksheet('members')
        self.setSheet = self.wb.worksheet('setting')
        self.WORKTIME = int(self.setSheet.cell(1, 2).value)
        self.members = self.memberSheet.col_values(1)
        self.demerits = []
        self.getDemerits()

    # 이름 가져오는 부분
    def getMembers(self):
        self.members.clear()
        self.members = self.memberSheet.col_values(1)

    # 벌점 가져오는 부분
    def getDemerits(self):
        self.demerits.clear()
        for i in range(1, len(self.members) + 1):
            self.demerits.append(int(self.memberSheet.cell(i, 2).value))

    def scheduleEveryDay(self):
        self.actSheet = self.wb.worksheet(str(time.MONTH) + '월')

        for i in range(len(self.members)):
            item = QTableWidgetItem('미출근')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            ui.tableWidget.setItem(i, 1, item)


class Ui_Dialog(object):
    def __init__(self):
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tab = QtWidgets.QWidget()
        self.label = QtWidgets.QLabel(self.tab)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.comboBox = QtWidgets.QComboBox(self.tab)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton_refresh = QtWidgets.QPushButton(self.tab)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tab_2 = QtWidgets.QWidget()
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.textEdit_2 = QtWidgets.QTextEdit(self.tab_2)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.textEdit_workHour = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_workMin = QtWidgets.QTextEdit(self.tab_2)
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.pushButton_workTime = QtWidgets.QPushButton(self.tab_2)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(339, 630)

        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 341, 631))
        self.tabWidget.setObjectName("tabWidget")

        self.tab.setObjectName("tab")

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

        self.label_2.setGeometry(QtCore.QRect(0, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.label_3.setGeometry(QtCore.QRect(85, 51, 241, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.tab, "")

        self.comboBox.setGeometry(QtCore.QRect(8, 91, 171, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.currentTextChanged.connect(self._pullComboText)

        self.pushButton.setGeometry(QtCore.QRect(190, 90, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self._pushButtonClicked)

        self.pushButton_refresh.setGeometry(QtCore.QRect(265, 90, 61, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.pushButton_refresh.setFont(font)
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.pushButton_refresh.clicked.connect(self._pushButton_refreshClicked)

        self.tableWidget.setGeometry(QtCore.QRect(5, 151, 321, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(len(gdrive.members))
        self.tableWidget.setHorizontalHeaderLabels(["이름", "출근시간", "벌점"])
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.tabWidget.addTab(self.tab, "")

        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.label_4.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.textEdit.setGeometry(QtCore.QRect(10, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")

        self.pushButton_2.setGeometry(QtCore.QRect(230, 50, 101, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self._pushButton2Clicked)

        self.pushButton_3.setGeometry(QtCore.QRect(230, 160, 101, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self._pushButton3Clicked)

        self.label_5.setGeometry(QtCore.QRect(10, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.textEdit_2.setGeometry(QtCore.QRect(10, 160, 211, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.label_6.setGeometry(QtCore.QRect(10, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.textEdit_workHour.setGeometry(QtCore.QRect(10, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit_workHour.setFont(font)
        self.textEdit_workHour.setObjectName("textEdit_workHour")

        self.textEdit_workMin.setGeometry(QtCore.QRect(130, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.textEdit_workMin.setFont(font)
        self.textEdit_workMin.setObjectName("textEdit_workMin")

        self.label_7.setGeometry(QtCore.QRect(85, 285, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8.setGeometry(QtCore.QRect(207, 285, 41, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.pushButton_workTime.setGeometry(QtCore.QRect(250, 280, 71, 51))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.pushButton_workTime.setFont(font)
        self.pushButton_workTime.setObjectName("pushButton_workTime")
        self.tabWidget.addTab(self.tab_2, "")
        self.pushButton_workTime.clicked.connect(self._pushButton_workTimeClicked)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "AILab 출근 기록기"))
        self.label.setText(_translate("Dialog", "AILab 출근 기록기"))
        self.label_2.setText(_translate("Dialog", "현재시간"))
        self.label_3.setText(_translate("Dialog", time.datetime.toString('yyyy.MM.dd hh:mm:ss')))
        self.pushButton.setText(_translate("Dialog", "출근"))
        self.pushButton_refresh.setText(_translate("Dialog", "새로\n고침"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "출근"))

        self.label_4.setText(_translate("Dialog", "인원 추가"))
        self.textEdit.setHtml(_translate("Dialog",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'맑은 고딕\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                         "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; vertical-align:middle;\">이름입력</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Dialog", "추가"))
        self.pushButton_3.setText(_translate("Dialog", "삭제"))
        self.label_5.setText(_translate("Dialog", "인원 삭제"))
        self.textEdit_2.setHtml(_translate("Dialog",
                                           "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                           "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                           "p, li { white-space: pre-wrap; }\n"
                                           "</style></head><body style=\" font-family:\'맑은 고딕\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                           "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\'; vertical-align:middle;\">이름입력</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "설정"))

        self.label_6.setText(_translate("Dialog", "출근 시간"))
        self.label_7.setText(_translate("Dialog", "시"))
        self.label_8.setText(_translate("Dialog", "분"))
        self.pushButton_workTime.setText(_translate("Dialog", "변경"))
        self.textEdit_workHour.setText("%02d" % (gdrive.WORKTIME // 60))
        self.textEdit_workMin.setText("%02d" % (gdrive.WORKTIME % 60))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "이름", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "출근시간", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "벌점", None))

        self.comboBox.addItems(gdrive.members)

    def initTable(self):
        today_rcd = gdrive.actSheet.col_values(time.DAY + 1)
        del today_rcd[0]

        for i in range(len(gdrive.members)):
            item = QTableWidgetItem(gdrive.members[i])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, item)

            item = QTableWidgetItem(today_rcd[i])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 1, item)

            item = QTableWidgetItem(str(gdrive.demerits[i]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(i, 2, item)

    def setTime(self):
        _translate = QtCore.QCoreApplication.translate
        self.label_3.setText(_translate("Dialog", time.datetime.toString('yyyy.MM.dd hh:mm:ss')))

    def _pushButtonClicked(self):
        if self.name in gdrive.members:
            index = gdrive.members.index(self.name)
            if self.tableWidget.item(index, 1).text() == '미출근':
                comHour = int(time.datetime.toString('hh'))
                comeMin = int(time.datetime.toString('mm'))
                comeTime = 60 * comHour + comeMin

                if comeTime - gdrive.WORKTIME > 0:
                    gdrive.demerits[index] = gdrive.demerits[index] + (comeTime - gdrive.WORKTIME - 1) // 10
                    item = QTableWidgetItem(str(gdrive.demerits[index]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(index, 2, item)

                item = QTableWidgetItem(time.datetime.toString('hh:mm:ss'))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(index, 1, item)

                telBot.sendMsg(telBot.chatId, time.datetime.toString('hh:mm:ss') + '\n' + self.name + '님이 출근했습니다.\n')

                cell = gdrive.actSheet.find(self.name)
                gdrive.actSheet.update_cell(cell.row, time.DAY + 1, time.datetime.toString('hh:mm:ss'))
                cell = gdrive.memberSheet.find(self.name)
                gdrive.memberSheet.update_cell(cell.row, 2, gdrive.demerits[index])

    def _pushButton2Clicked(self):
        newMember = self.textEdit.toPlainText()
        num_members = len(gdrive.members)

        if newMember != '이름입력':
            gdrive.memberSheet.update_cell(num_members + 1, 1, newMember)
            gdrive.memberSheet.update_cell(num_members + 1, 2, 0)

            lastday = calendar.monthrange(time.YEAR, time.MONTH)[1]

            gdrive.actSheet.update_cell(num_members + 2, 1, newMember)

            cell_tmp = gdrive.actSheet.row_values(2)
            del cell_tmp[0]
            
            cell_list = gdrive.actSheet.range(num_members + 2, 2, num_members + 2, lastday + 1)
            for i in range(len(cell_list)):
                if cell_tmp[i] == '휴일':
                    cell_list[i].value = '휴일'
                else:
                    cell_list[i].value = '미출근'
            gdrive.actSheet.update_cells(cell_list)

            gdrive.getMembers()
            gdrive.getDemerits()

            num_members = len(gdrive.members)

            self.comboBox.addItems(gdrive.members)

            self.tableWidget.setRowCount(num_members)
            row = self.tableWidget.rowCount()

            item = QTableWidgetItem(gdrive.members[-1])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row - 1, 0, item)

            item = QTableWidgetItem(str(gdrive.demerits[-1]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row - 1, 2, item)

            item = QTableWidgetItem('미출근')
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row - 1, 1, item)

            QMessageBox.about(Dialog, '추가 완료', "'" + newMember + "'" + '을(를) 추가했습니다.')
        else:
            QMessageBox.about(Dialog, '추가 실패', '이름을 입력해주세요')

    def _pushButton3Clicked(self):
        delMember = self.textEdit_2.toPlainText()
        if delMember != '이름입력':
            try:
                cell = gdrive.memberSheet.find(delMember)
                gdrive.memberSheet.delete_row(cell.row)
                cell = gdrive.actSheet.find(delMember)
                gdrive.actSheet.delete_row(cell.row)

                tmpSheet = gdrive.wb.get_worksheet(-1)
                if gdrive.actSheet.title != tmpSheet.title:
                    cell = tmpSheet.find(delMember)
                    tmpSheet.delete_row(cell.row)

                for i in range(self.tableWidget.rowCount()):
                    if self.tableWidget.item(i, 0).text() == delMember:
                        self.tableWidget.removeRow(i)
                        break

                gdrive.getMembers()
                gdrive.getDemerits()

                self.comboBox.addItems(gdrive.members)
                self.tableWidget.setRowCount(len(gdrive.members))
                QMessageBox.about(Dialog, '삭제 완료', "'" + delMember + "'" + '을(를) 삭제했습니다.')
            except gspread.exceptions.CellNotFound:
                QMessageBox.about(Dialog, '삭제 실패', '없는 사람 입니다.')
        else:
            QMessageBox.about(Dialog, '삭제 실패', '이름을 입력해주세요')

    def _pushButton_workTimeClicked(self):
        hour = int(self.textEdit_workHour.toPlainText())
        min = int(self.textEdit_workMin.toPlainText())
        gdrive.WORKTIME = 60 * hour + min

        gdrive.setSheet.update_cell(1, 2, gdrive.WORKTIME)

        msg = '출근시간을 %02d시 %02d분으로 변경했습니다.' % (hour, min)

        QMessageBox.about(Dialog, '변경 완료', msg)

    def _pushButton_refreshClicked(self):
        gdrive.getDemerits()
        datas = gdrive.actSheet.col_values(time.DAY + 1)
        del datas[0]

        for row in range(len(datas)):
            item = QTableWidgetItem(datas[row])
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, 1, item)

            item = QTableWidgetItem(str(gdrive.demerits[row]))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.setItem(row, 2, item)

        QMessageBox.about(Dialog, '완료', '새로고침 되었습니다.')

    def _pullComboText(self, text):
        self.name = text


if __name__ == "__main__":
    telBot = TelBot()
    time = Time()
    gdrive = GDrive()

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.initTable()

    sched = BackgroundScheduler()
    sched.add_job(ui.setTime, IntervalTrigger(seconds=1), id='setTime')
    sched.add_job(time.getDate, IntervalTrigger(seconds=1), id='getDate')
    sched.add_job(gdrive.scheduleEveryDay, CronTrigger(hour='0', minute='1', second='0'), id='scheduleEveryDay')
    sched.start()

    sys.exit(app.exec_())