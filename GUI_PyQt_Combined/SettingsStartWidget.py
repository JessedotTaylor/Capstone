# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FileLoader import SettingsFile


class Ui_Settings(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str, str)
    
    def __init__(self, filename):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Form")
        
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1281, 1031))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_21.addItem(spacerItem1)
        self.BackButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.BackButton.setFont(font)
        self.BackButton.setObjectName("BackButton")
        self.horizontalLayout_21.addWidget(self.BackButton)
        self.BackButton.clicked.connect(lambda: self.switch('back'))

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_21.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)

        self.RootDirLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.RootDirLineEdit.setObjectName("RootDirLineEdit")
        self.horizontalLayout_10.addWidget(self.RootDirLineEdit)
        self.RootDirLineEdit.editingFinished.connect(lambda: self.editied('Root_Directory', self.RootDirLineEdit.text()))

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem6)

        self.NetworkDirLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.NetworkDirLineEdit.setObjectName("NetworkDirLineEdit")
        self.horizontalLayout_9.addWidget(self.NetworkDirLineEdit)
        self.NetworkDirLineEdit.editingFinished.connect(lambda: self.editied('Network_Directory', self.NetworkDirLineEdit.text()))

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)

        self.PresetsDirLineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.PresetsDirLineEdit.setObjectName("PresetsDirLineEdit")
        self.horizontalLayout_8.addWidget(self.PresetsDirLineEdit)
        self.PresetsDirLineEdit.editingFinished.connect(lambda: self.editied('Presets_Directory', self.PresetsDirLineEdit.text()))

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_12.addItem(spacerItem14)
        self.verticalLayout.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_20.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem17)
        self.verticalLayout.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_19.addItem(spacerItem18)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_17.addItem(spacerItem19)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_16.addItem(spacerItem20)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_15.addItem(spacerItem21)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        # spacerItem22 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # self.horizontalLayout_14.addItem(spacerItem22)

        self.bkCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.bkCheckBox.setChecked(True)
        self.bkCheckBox.setObjectName("bkCheckBox")
        self.horizontalLayout_14.addWidget(self.bkCheckBox)
        self.bkCheckBox.clicked.connect(lambda: self.editied('use_background', True if self.bkCheckBox.checkState() > 0 else False))

        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.FullScreenCheckBox = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.FullScreenCheckBox.setChecked(True)
        self.FullScreenCheckBox.setObjectName("FullScreenCheckBox")
        self.verticalLayout_3.addWidget(self.FullScreenCheckBox)
        self.FullScreenCheckBox.clicked.connect(lambda: self.fullScreenChecked(self.FullScreenCheckBox.checkState()))

        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_5.setEnabled(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_22.addWidget(self.label_5)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem23)

        self.widthLineBox = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.widthLineBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widthLineBox.sizePolicy().hasHeightForWidth())
        self.widthLineBox.setSizePolicy(sizePolicy)
        self.widthLineBox.setObjectName("widthLineBox")
        self.widthLineBox.editingFinished.connect(lambda: self.editied('Width', self.widthLineBox.text()))

        self.horizontalLayout_22.addWidget(self.widthLineBox)
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_22.addWidget(self.label_6)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem24)

        self.heightLineBox = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.heightLineBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.heightLineBox.sizePolicy().hasHeightForWidth())
        self.heightLineBox.setSizePolicy(sizePolicy)
        self.heightLineBox.setObjectName("heightLineBox")
        self.horizontalLayout_22.addWidget(self.heightLineBox)
        self.heightLineBox.editingFinished.connect(lambda: self.editied('Height', self.heightLineBox.text()))
        

        # self.RestartText = QtWidgets.QLabel(self.horizontalLayoutWidget)
        # self.RestartText.setEnabled(True)
        # self.RestartText.setObjectName("RestartText")
        # self.horizontalLayout_22.addWidget(self.RestartText)
        self.verticalLayout_3.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_13.addItem(spacerItem25)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.DefaultsButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.DefaultsButton.setFont(font)
        self.DefaultsButton.setObjectName("DefaultsButton")
        self.horizontalLayout_11.addWidget(self.DefaultsButton)
        self.DefaultsButton.clicked.connect(self.defaultsClicked)


        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem26)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem27)

        self.retranslateUi()
        self.rootFile = filename
        self.settingsObj = SettingsFile(filename)
        self.setValues(self.settingsObj.json)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.BackButton.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "Settings"))
        self.label_2.setText(_translate("Form", "Root Directory:"))
        self.label_3.setText(_translate("Form", "Network Directory:"))
        self.label_4.setText(_translate("Form", "Presets Directory:"))
        self.FullScreenCheckBox.setText(_translate("Form", " Full Screen Mode"))
        self.bkCheckBox.setText(_translate("Form", "Use Background"))
        self.label_5.setText(_translate("Form", "Width:"))
        self.label_6.setText(_translate("Form", "Height:"))
#         self.RestartText.setText(_translate("Form", "(Change Requires\n"
# "Restart)"))
        self.DefaultsButton.setText(_translate("Form", "Restore Defaults"))

    def switch(self, switchTo):
        self.switch_window.emit(switchTo, "settings")
    
    def defaultsClicked(self):
        # print("restore Defaults Clicked")
        self.settingsObj.resetDefaults()
        self.setValues(self.settingsObj.json)
    
    def fullScreenChecked(self, val):
        print("Check Box Status: {}".format(val))
        val = val > 0
        if val:
            self.widthLineBox.setEnabled(False)
            self.heightLineBox.setEnabled(False)
        else:
            self.widthLineBox.setEnabled(True)
            self.heightLineBox.setEnabled(True)

        self.settingsObj.setParam('Full_Screen_Mode', val)


    def editied(self, lineBox, value):
        print("Linebox '{}' changed to text '{}'".format(lineBox, value))
        self.settingsObj.setParam(lineBox, value)

    def setValues(self, jsonDic):
        self.RootDirLineEdit.setText(self.settingsObj.getRoot())
        self.NetworkDirLineEdit.setText(self.settingsObj.getNetwork())
        self.PresetsDirLineEdit.setText(self.settingsObj.getPreset())
        self.bkCheckBox.setChecked(self.settingsObj.getBk())

        if self.settingsObj.getFullScreen(): #True
            self.FullScreenCheckBox.setChecked(True)
            self.widthLineBox.setEnabled(False)
            self.heightLineBox.setEnabled(False)
        else:
            self.FullScreenCheckBox.setChecked(False)
            self.widthLineBox.setEnabled(True)
            self.widthLineBox.setText(str(self.settingsObj.getWidth()))
            self.heightLineBox.setEnabled(True)
            self.heightLineBox.setText(str(self.settingsObj.getHeight()))

    def resizeFunc(self,width, height):
        self.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Settings("GUI_PyQt_Combined/Settings/settings.json")
    ui.resizeFunc(1240,1024)
    ui.show()
    sys.exit(app.exec_())
