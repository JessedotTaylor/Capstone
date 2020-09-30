from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtGui
from PyQt5 import QtCore
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]

        #-------------------------------------------------------
        # Setting Background Colour

        # self.graphWidget.setBackground('w')
        # self.graphWidget.setBackground('#bbccaa') 

        # self.graphWidget.setBackground((100,50,255))      # RGB each 0-255
        # self.graphWidget.setBackground((100,50,255,25))   # RGBA (A = alpha opacity)
        
        # self.graphWidget.setBackground(QtGui.QColor(100,50,254,25)) # Requires from PyQt5 import QtGui

        # color = self.palette().color(QtGui.QPalette.Window)  # Get the default window background,
        # self.graphWidget.setBackground(color)
        #-----------------------------------------------------------------
        
        #-----------------------------------------------------------------
        # Change Line render style
        # pen = pg.mkPen(color=(255, 0, 0), width=15, style=QtCore.Qt.DashLine)

        # # plot data: x, y values
        # self.graphWidget.plot(hour, temperature, pen=pen)
        #------------------------------------------------------------------

        #------------------------------------------------------------------
        # Add marker symbols to plot points (Options are o, s, t, d, +, QPainterPath)
        #self.graphWidget.plot(hour, temperature, symbol='+', symbolSize=30, symbolBrush=('b'))
        #------------------------------------------------------------------

        #------------------------------------------------------------------
        # Add Titles and Axis labels
        # self.graphWidget.setTitle("Your Title Here", color="b", size="30pt")

        # # styles = {'color':'r', 'font-size':'20px'}
        # # self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        # # self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)

        # self.graphWidget.setLabel('left', "<span style=\"color:red;font-size:20px\">Temperature (°C)</span>")
        # self.graphWidget.setLabel('bottom', "<span style=\"color:red;font-size:20px\">Hour (H)</span>")
        #------------------------------------------------------------------

        self.graphWidget.plot(hour, temperature)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()