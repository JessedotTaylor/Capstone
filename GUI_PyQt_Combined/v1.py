import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import PresetStartWidget, MainWindowWidget, FileStartWidget, DiskStartWidget

class Controller:
    def __init__(self):
        self.showMainWindow()
        

    def showMainWindow(self):
        self.main = MainWindowWidget.Ui_MainWindow()
        # Connect 4 buttons here
        #self.main.switch_window
        self.main.switch_window.connect(self._switchToMain)
        self.main.show()

    def _switchToMain(self, text):
        print("_switchToMain called: {}".format(text))
        if text == "preset":
            self.showPresetStartWidget()
        if text == "disk":
            self.showDiskStartWidget("Local Disk")
        if text == "network":
            self.showDiskStartWidget("Network Location")    

    def showDiskStartWidget(self, srcDir):
        self.file = DiskStartWidget.Ui_DiskStartWidget("C:\\")
        self.file.setSrcDir(srcDir)
        #Button Connections
        self.file.switch_window.connect(self._switchToSecond)
        self.main.close()
        self.file.show()

    def showPresetStartWidget(self):
        self.preset = PresetStartWidget.Ui_Form()
        self.preset.switch_window.connect(self._switchToSecond)
        self.main.close()
        self.preset.show()

    def _switchToSecond(self, text, src):
        print("_switchToSecond called: {}, src: {}".format(text, src))
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
        self.start = FileStartWidget.Ui_FileStartWidget()
        self.start.show()



def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.showMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()