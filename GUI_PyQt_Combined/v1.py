import sys, shutil
from PyQt5 import QtCore, QtGui, QtWidgets
import PresetStartWidget, MainWindowWidget, FileStartWidget, DiskStartWidget, SettingsStartWidget

class bk(QtWidgets.QWidget):
    def __init__(self, width, height):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("Background")
        self.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))
        
    

class Controller:
    def __init__(self,settingsFile='GUI_PyQt_Combined/Settings/settings.json'):
        import platform
        os = platform.system()
        self.loadSettings(settingsFile)
        self.showMainWindow()

    def loadSettings(self, filename):
        print("Load settings called")
        settings = SettingsStartWidget.Ui_Settings(filename)
        settingsObj = settings.settingsObj
        self.DiskFilePath = settingsObj.getRoot()
        self.NetworkFilePath = settingsObj.getNetwork()
        self.PresetFilePath = settingsObj.getPreset()
        self.fullScreenMode = settingsObj.getFullScreen()
        self.width = settingsObj.getWidth()
        self.height = settingsObj.getHeight()
        self.showGreyBack = settingsObj.getBk()
        if self.showGreyBack:
            self.setupGreyBack(self.width, self.height)
        self.settings = settings
        self.settingsObj = settingsObj

        
    def setupGreyBack(self, width, height):
        self.bk = bk(width, height)
        self.bk.show()
        if self.fullScreenMode:
            self.bk.showFullScreen()
        
        

    def showMainWindow(self):
        self.main = MainWindowWidget.Ui_MainWindow(self.width, self.height)
        # Connect 4 buttons here
        #self.main.switch_window
        self.main.switch_window.connect(self._switchToMain)
        if self.fullScreenMode:
            self.main.showFullScreen()
        self.main.show()

    def _switchToMain(self, text):
        print("_switchToMain called: {}".format(text))
        self.main.close()
        if text == "preset":
            self.showDiskStartWidget(self.PresetFilePath, text)
        elif text == "file":
            self.showDiskStartWidget(self.DiskFilePath, text)
        elif text == "network":
            self.showDiskStartWidget(self.NetworkFilePath, text)    #Temp hack for presentaion
        elif text == "settings":
            self.showSettingsStartWidget()

    def showDiskStartWidget(self, srcDir, root):
        self.file = DiskStartWidget.Ui_DiskStartWidget(srcDir, self.width, self.height, root, root!='preset')
        #Button Connections
        self.file.switch_window.connect(self._switchToSecond)
        self.file.save_preset.connect(self._saveAsPreset)
        if self.fullScreenMode:
            self.file.showFullScreen()
        # self.main.close()
        self.file.show()
    
    def _saveAsPreset(self, path):
        print("_SaveAsPreset Called, path: {}".format(path))
        print("Copying File {} to Presets Folder ({})".format(path.split('/')[-1], self.PresetFilePath))
        _translate = QtCore.QCoreApplication.translate
        self.file.copyStatusLabel.setText(_translate("DiskStartWidget", "Copying File {} to Presets Folder ({})".format(path.split('/')[-1], self.PresetFilePath)))
        
        try:
            shutil.copy2(path, self.PresetFilePath)
            self.file.copyStatusLabel.setText(_translate("DiskStartWidget", "Copy successful! File {} now in Presets Folder ({})".format(path.split('/')[-1], self.PresetFilePath)))
        except shutil.SameFileError as e:
            self.file.copyStatusLabel.setText(_translate("DiskStartWidget", "Copy Failed! Reason: {}".format(e)))
        


    def showSettingsStartWidget(self):
        self.settings.resizeFunc(self.width, self.height)
        self.settings.switch_window.connect(self._switchToSecond)
        if self.fullScreenMode:
            self.settings.showFullScreen()
        
        self.settings.show()

    # def showPresetStartWidget(self, srcDir, root):
    #     print("Show Preset widget called")
    #     self.file = DiskStartWidget.Ui_DiskStartWidget(srcDir, self.width, self.height, root, showPresetButton=False) #Temp hotfix for presentation
    #     # self.preset = PresetStartWidget.Ui_Form() #Temp hotfix for presentation
    #     self.file.switch_window.connect(self._switchToSecond)
    #     self.file.showFullScreen()
    #     # self.main.close()
    #     self.file.show()
    

    def _switchToSecond(self, text, src):
        print("_switchToSecond called: {}, src: {}".format(text, src))
        self.root = src
        if src != 'settings':
            self.file.close()
        else:
            self.settings.close()
            if self.settingsObj.getChanges(): #Check settings haven't changed / reload if have
                self.loadSettings(self.settingsObj.filename)
            
        
        if text == 'back':
            self.showMainWindow()
        elif text == 'next':
            self.showStartWidget()

    def showStartWidget(self):
        
        print("Show Start widget called")
        self.start = FileStartWidget.Ui_FileStartWidget(self.width, self.height)
        self.start.updateScreen(self.file.path)
        self.start.switch_window.connect(self._switchToRunning)
        self.start.show()
        if self.fullScreenMode:
            self.start.showFullScreen()

    def _switchToRunning(self, text):
        self.start.close()
        print("_switchToRunning Called: {}, src: {}".format(text, self.root))
        if text == 'back':
            self._switchToMain(self.root)
            # #print("Back")
            # if self.root == "preset":
            #     self.showPresetStartWidget(self.startFilePath + "/Presets/", "preset")
            # elif self.root == "file":
            #     #print("File")
            #     self.showDiskStartWidget(self.startFilePath, "file")
            # elif self.root == "network":
            #     self.showDiskStartWidget(self.startFilePath + "/NetworkFiles/", "network")    #Temp hack for presentaion
        
        elif text == 'start':
            print("Start called")
            self.main.close()
            self.bk.close()
            #self.showRunningWidget()

        



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()