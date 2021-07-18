from PyQt5 import QtCore, QtGui, QtWidgets
import dwm_module,subprocess,sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DWMOFF = QtWidgets.QPushButton(self.centralwidget)
        self.DWMOFF.setGeometry(QtCore.QRect(180, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setBold(True)
        font.setWeight(75)
        self.DWMOFF.setFont(font)
        self.DWMOFF.setObjectName("DWMOFF")
        self.DWMON = QtWidgets.QPushButton(self.centralwidget)
        self.DWMON.setGeometry(QtCore.QRect(40, 320, 75, 23))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setBold(True)
        font.setWeight(75)
        self.DWMON.setFont(font)
        self.DWMON.setObjectName("DWMON")
        self.DWMManager = QtWidgets.QLabel(self.centralwidget)
        self.DWMManager.setGeometry(QtCore.QRect(60, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setBold(True)
        font.setWeight(75)
        self.DWMManager.setFont(font)
        self.DWMManager.setObjectName("DWMManager")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 50, 250, 191))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.DWMStatus = QtWidgets.QLabel(self.centralwidget)
        self.DWMStatus.setGeometry(QtCore.QRect(110, 280, 70, 12))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setBold(True)
        font.setWeight(75)
        self.DWMStatus.setFont(font)
        self.DWMStatus.setObjectName("DWMStatus")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.DWMON.clicked.connect(self.on)
        self.DWMOFF.clicked.connect(self.off)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DWMOFF.setText(_translate("MainWindow", "OFF"))
        self.DWMON.setText(_translate("MainWindow", "ON"))
        self.DWMManager.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">DWM Manager</span></p></body></html>"))
        self.DWMStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">DWM : <span>ON</span></p></body></html>"))
    def on(self):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.clear()
        self.textBrowser.append('DWM 활성화중..')
        a = dwm_module.DWMstate('ON')
        if a == 'PASS':
            self.textBrowser.append('DWM 활성화 성공!')
            self.DWMStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">DWM : <span>ON</span></p></body></html>"))
        elif a == 'ERROR_DWM':
            self.textBrowser.append('DWM이 이미 실행되고 있습니다.')
        else:
            self.textBrowser.append('DWM 활성화 실패..')

        
    def off(self):
        _translate = QtCore.QCoreApplication.translate
        self.textBrowser.clear()
        self.textBrowser.append('DWM 비활성화중..')
        a = dwm_module.DWMstate('OFF')
        if a == 'PASS':
            self.textBrowser.append('DWM 비활성화 성공!')
            self.DWMStatus.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">DWM : <span style=\" color:#ff0000;\">OFF</span></p></body></html>"))
        elif a == 'ERROR_DWM':
            self.textBrowser.append('DWM이 이미 종료되었습니다.')
        else:
            self.textBrowser.append('DWM 비활성화 실패..')

if __name__ == "__main__":
    output =  subprocess.getoutput
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())