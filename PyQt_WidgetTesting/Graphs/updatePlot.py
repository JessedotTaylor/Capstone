from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))
        self.y = [randint(0, 100) for _ in range(100)]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))

        # plot data: x, y values
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        #self.graphWidget.plot(hour, temperature)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        #self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        #self.y = self.y[1:]
        self.y.append(randint(0,100))

        self.data_line.setData(self.x, self.y)


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()