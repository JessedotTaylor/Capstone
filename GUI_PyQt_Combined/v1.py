import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PresetStartWidget, MainWindowWidget, FileStartWidget, DiskStartWidget

class Controller:
    def __init__(self):
        import platform
        os = platform.system()
        if os == 'Darwin':
            self.startFilePath = '/Users/jessetaylor Mk3/Desktop'
        elif os == 'Windows':
            self.startFilePath = 'C:\\'
        elif os == 'Linux':
            self.startFilePath = '/home/pi/Documents/GUI_PyQt_Combined'
        self.width = 1280
        self.height = 900
        self.showMainWindow()
        

    def showMainWindow(self):
        self.main = MainWindowWidget.Ui_MainWindow(self.width, self.height)
        # Connect 4 buttons here
        #self.main.switch_window
        self.main.switch_window.connect(self._switchToMain)
        self.main.show()

    def _switchToMain(self, text):
        print("_switchToMain called: {}".format(text))
        self.main.close()
        if text == "preset":
            self.showPresetStartWidget(self.startFilePath + "/Presets/")
        if text == "disk":
            self.showDiskStartWidget(self.startFilePath)
        if text == "network":
            self.showDiskStartWidget(self.startFilePath + "/NetworkFiles/")    #Temp hack for presentaion

    def showDiskStartWidget(self, srcDir):
        self.file = DiskStartWidget.Ui_DiskStartWidget(srcDir, self.width, self.height)
        self.file.setSrcDir(srcDir)
        #Button Connections
        self.file.switch_window.connect(self._switchToSecond)
        # self.main.close()
        self.file.show()

    def showPresetStartWidget(self, srcDir):
        self.file = DiskStartWidget.Ui_DiskStartWidget(srcDir, self.width, self.height, showPresetButton=False) #Temp hotfix for presentation
        # self.preset = PresetStartWidget.Ui_Form() #Temp hotfix for presentation
        self.file.switch_window.connect(self._switchToSecond)
        # self.main.close()
        self.file.show()
    

    def _switchToSecond(self, text, src):
        print("_switchToSecond called: {}, src: {}".format(text, src))
        self.root = src
        if src == 'preset':
            self.preset.close()
        elif src == 'file':
            self.file.close()
        
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

    def _switchToRunning(self, text):
        self.start.close()
        print("_switchToRunning Called: {}, src {}".format(text, self.root))
        if text == 'back':
            if self.root == 'preset':
                self.showPresetStartWidget()
            elif self.root == 'file':
                self.showDiskStartWidget("Z:/Capstone/Python/GUI_PyQt_Combined/Presets") #Handling for previous source directory?
        
        elif text == 'start':
            print("Start called")
            #self.showRunningWidget()

        



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()