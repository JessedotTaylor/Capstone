#https://www.youtube.com/watch?v=Vde5SH8e1OQ
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    xpos, ypos = 0,100
    widthPx = 1280
    heightPx = 1024
    win.setGeometry(xpos, ypos, widthPx, heightPx)
    win.setWindowTitle("Main Window")

    label = QtWidgets.QLabel(win)
    label.setText("My First Label")
    label.move(50,50)


    win.show()
    sys.exit(app.exec_())

window()