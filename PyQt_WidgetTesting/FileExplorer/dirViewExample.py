from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
import sys
# QFileSystemModel model()
# model.setRootPath("")

# QTreeView tree
# tree.setModel(model)

# tree.setAnimated(False)
# tree.setIndentaion(20)
# tree.setSortingEnabled(True)
# availableSize = tree.screen().availableGeometry().size()
# tree.resize(availableSize/2)
# tree.setColumnWidth(0, tree.width() /3)

# tree.setWindowTitle("Dir View")

class filedialogdemo(QWidget):
   def __init__(self, parent = None):
      super(filedialogdemo, self).__init__(parent)
		
      layout = QVBoxLayout()
      self.btn = QPushButton("QFileDialog static method demo")
      self.btn.clicked.connect(self.getfile)
		
      layout.addWidget(self.btn)
      self.le = QLabel("Hello")
		
      layout.addWidget(self.le)
      self.btn1 = QPushButton("QFileDialog object")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)
		
      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)
      self.setWindowTitle("File Dialog demo")
		
   def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
            'c:\\',"Image files (*.jpg *.gif)")
        imgPath = fname[0]
        pixMap = QPixmap(imgPath)

        self.le.setPixmap(pixMap)
        # self.le.setPixmap(QPixmap(pixMap))
        #self.le.setPixmap(QPixmap('May I ask for one final thing.PNG'))
		
   def getfiles(self):
    #   dlg = QFileDialog()
    #   dlg.setFileMode(QFileDialog.AnyFile)
    #   dlg.setFilter("Text files (*.txt)")
        dlg = QFileDialog(self, 'Open Files', 'C:\\', "Text files (*.txt)")
        #filenames = QStringList()
            
        if dlg.exec_():
            filenames = dlg.selectedFiles()
            f = open(filenames[0], 'r')
                
            with f:
                data = f.read()
                self.contents.setText(data)

class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        appWidth = 800
        appHeight = 300
        self.setWindowTitle('File System Viewer')
        self.setGeometry(300, 300, appWidth, appHeight)

        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)
        self.tree =  QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dirPath))
        self.tree.setColumnWidth(0, 250)
        self.tree.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)
        self.setLayout(layout)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	dirPath = "C:\\"
	demo = FileSystemView(dirPath)
	demo.show()
	sys.exit(app.exec_())

# def main():
#    app = QApplication(sys.argv)
#    ex = filedialogdemo()
#    ex.show()
#    sys.exit(app.exec_())
	
# if __name__ == '__main__':
#    main()