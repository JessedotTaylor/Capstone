# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DiskStartWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_DiskStartWidget(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str, str)
    save_preset = QtCore.pyqtSignal(str)

    def __init__(self, dirPath, width, height, root, showPresetButton=True):
        self.showPresetButton = showPresetButton
        self.root = root
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("DiskStartWidget")
        self.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.backButton.sizePolicy().hasHeightForWidth())
        self.backButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setCheckable(False)
        self.backButton.setChecked(False)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_3.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.switch("back"))

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.model = QtWidgets.QFileSystemModel() 
        self.model.setRootPath(dirPath)
        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirPath))
        self.tree.setColumnWidth(0, 1024//4)
        self.tree.setAlternatingRowColors(True)
        self.tree.clicked.connect(self.onClicked)

        self.horizontalLayout_2.addWidget(self.tree)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.backButton.setFont(font)
        self.copyStatusLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.copyStatusLabel.setObjectName("copyStatusLabel")
        self.horizontalLayout.addWidget(self.copyStatusLabel)

        
        if showPresetButton:
            self.SaveAsPresetButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.SaveAsPresetButton.sizePolicy().hasHeightForWidth())
            self.SaveAsPresetButton.setSizePolicy(sizePolicy)
            font = QtGui.QFont()
            font.setPointSize(16)
            self.SaveAsPresetButton.setFont(font)
            self.SaveAsPresetButton.setObjectName("SaveAsPresetButton")
            self.horizontalLayout.addWidget(self.SaveAsPresetButton)
            self.SaveAsPresetButton.clicked.connect(self.savePreset)
            self.SaveAsPresetButton.setEnabled(False)

        self.NextButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.NextButton.setFont(font)
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout.addWidget(self.NextButton)
        self.NextButton.clicked.connect(lambda: self.switch("next"))
        self.NextButton.setEnabled(False)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName()

        self.supportedFiles = ['csv'] # 'txt', 'json'?

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("DiskStartWidget", "Form"))
        self.backButton.setText(_translate("DiskStartWidget", "Back"))
        if self.showPresetButton:
            self.SaveAsPresetButton.setText(_translate("DiskStartWidget", "Save As Preset"))
        self.NextButton.setText(_translate("DiskStartWidget", "Next Button"))
        # self.copyStatusLabel.setText(_translate("DiskStartWidget", "Hellow WOrld"))

    def setSrcDir(self, srcDir):
        print("Set Source Dir called: {}".format(srcDir))

    def switch(self, switchTo):
        self.switch_window.emit(switchTo, self.root)

    def savePreset(self):
        print("Save selected preset called")
        self.save_preset.emit(self.path)
    
    def onClicked(self, index):
        # self.sender() == self.treeView
        # self.sender().model() == self.fileSystemModel
        path = self.sender().model().filePath(index)
        obj = path.split('.')
        print(obj)
        if len(obj) > 1 and obj[-1] in self.supportedFiles:
            if self.showPresetButton:
                self.SaveAsPresetButton.setEnabled(True)
            self.NextButton.setEnabled(True)
            self.path = path
        else: 
            if self.showPresetButton:
                self.SaveAsPresetButton.setEnabled(False)
            self.NextButton.setEnabled(False)



if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # controller = Controller()
    # controller.show_login()
    # sys.exit(app.exec_())
    
    app = QtWidgets.QApplication(sys.argv)
    import platform
    os = platform.system()
    if os == 'Darwin':
        startFilePath = '/Users/jessetaylor Mk3/Desktop'
    elif os == 'Windows':
        startFilePath = 'C:\\'
    elif os == 'Linux':
        startFilePath = '/home/pi/Documents/GUI_PyQt_Combined'
    win = Ui_DiskStartWidget(startFilePath, 1240,1024,'usr')

    win.show()
    sys.exit(app.exec_())