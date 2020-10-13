from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QWidget):

        switch_window = QtCore.pyqtSignal(str)
        # switch_window_File = QtCore.pyqtSignal(str)
        # switch_window_Preset = QtCore.pyqtSignal(str)
        # switch_window_Network = QtCore.pyqtSignal(str)
        # switch_window_Settings = QtCore.pyqtSignal(str)

        def __init__(self, width, height):
                QtWidgets.QWidget.__init__(self)
                self.setObjectName("MainWindow")
                self.resize(width, height)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
                self.setSizePolicy(sizePolicy)
                self.setMinimumSize(QtCore.QSize(width, height))
                self.setMaximumSize(QtCore.QSize(width, height))
                self.centralwidget = QtWidgets.QWidget(self)
                self.centralwidget.setEnabled(True)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
                self.centralwidget.setSizePolicy(sizePolicy)
                self.centralwidget.setMinimumSize(QtCore.QSize(1280, 0))
                self.centralwidget.setObjectName("centralwidget")
                self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
                self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 981))
                self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
                self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
                self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
                self.horizontalLayout.setObjectName("horizontalLayout")
                self.verticalLayout_2 = QtWidgets.QVBoxLayout()
                self.verticalLayout_2.setObjectName("verticalLayout_2")

                self.presetButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.presetButton.sizePolicy().hasHeightForWidth())
                self.presetButton.setSizePolicy(sizePolicy)
                self.presetButton.setMinimumSize(QtCore.QSize(400, 75))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.presetButton.setFont(font)
                self.presetButton.setIconSize(QtCore.QSize(16, 16))
                self.presetButton.setCheckable(False)
                self.presetButton.setChecked(False)
                self.presetButton.setObjectName("presetButton")
                self.verticalLayout_2.addWidget(self.presetButton, 0, QtCore.Qt.AlignHCenter)
                self.presetButton.clicked.connect(lambda: self.switch("preset"))

                self.networkButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.networkButton.sizePolicy().hasHeightForWidth())
                self.networkButton.setSizePolicy(sizePolicy)
                self.networkButton.setMinimumSize(QtCore.QSize(400, 75))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.networkButton.setFont(font)
                self.networkButton.setObjectName("networkButton")
                self.verticalLayout_2.addWidget(self.networkButton, 0, QtCore.Qt.AlignHCenter)
                self.horizontalLayout.addLayout(self.verticalLayout_2)
                self.verticalLayout = QtWidgets.QVBoxLayout()
                self.verticalLayout.setObjectName("verticalLayout")
                self.networkButton.clicked.connect(lambda: self.switch("network"))

                self.diskButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.diskButton.sizePolicy().hasHeightForWidth())
                self.diskButton.setSizePolicy(sizePolicy)
                self.diskButton.setMinimumSize(QtCore.QSize(400, 75))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.diskButton.setFont(font)
                self.diskButton.setObjectName("diskButton")
                self.verticalLayout.addWidget(self.diskButton, 0, QtCore.Qt.AlignHCenter)
                self.diskButton.clicked.connect(lambda: self.switch("file"))

                self.settingsButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
                sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(self.settingsButton.sizePolicy().hasHeightForWidth())
                self.settingsButton.setSizePolicy(sizePolicy)
                self.settingsButton.setMinimumSize(QtCore.QSize(400, 75))
                font = QtGui.QFont()
                font.setPointSize(16)
                self.settingsButton.setFont(font)
                self.settingsButton.setObjectName("settingsButton")
                self.verticalLayout.addWidget(self.settingsButton, 0, QtCore.Qt.AlignHCenter)
                self.settingsButton.clicked.connect(lambda: self.switch("settings"))

                self.horizontalLayout.addLayout(self.verticalLayout)
                self.menubar = QtWidgets.QMenuBar(self)
                self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
                self.menubar.setObjectName("menubar")
                self.statusbar = QtWidgets.QStatusBar(self)
                self.statusbar.setObjectName("statusbar")

                self.retranslateUi()
                # QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.presetButton.setText(_translate("MainWindow", "Load From\n"
        "Preset"))
                self.networkButton.setText(_translate("MainWindow", "Load From\n"
        "Network"))
                self.diskButton.setText(_translate("MainWindow", "Load From\n"
        "File / Disk"))
                self.settingsButton.setText(_translate("MainWindow", "Settings\n"
        ""))

        def switch(self, switchTo):
                # if switchTo == 'preset':
                #         self.switch_window_Preset.emit()
                self.switch_window.emit(switchTo)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()

    win.show()
    sys.exit(app.exec_())
