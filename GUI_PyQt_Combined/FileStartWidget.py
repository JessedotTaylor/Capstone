import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import FileLoader


class Ui_FileStartWidget(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, width, height):
        QtWidgets.QWidget.__init__(self)
        self.setObjectName("FileStartWidget")
        self.resize(width, height)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(width, height))
        self.setMaximumSize(QtCore.QSize(width, height))
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, width, height))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.presetName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.presetName.setObjectName("presetName")
        self.verticalLayout_3.addWidget(self.presetName)
        self.presetDetails = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.presetDetails.setObjectName("presetDetails")
        self.verticalLayout_3.addWidget(self.presetDetails)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.graphWidget = pg.GraphicsLayoutWidget()
        self.graphWidget.setObjectName("graphWidget")
        self.horizontalLayout_3.addWidget(self.graphWidget)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_2.addWidget(self.backButton)
        self.backButton.clicked.connect(lambda: self.switch('back'))

        self.startButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_2.addWidget(self.startButton)
        self.startButton.clicked.connect(lambda: self.switch("start"))

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("FileStartWidget", "Form"))
        self.presetName.setText(_translate("FileStartWidget", "Working File Name"))
        self.presetDetails.setText(_translate("FileStartWidget", "Working File Details \neg: Run Time, Max Temp, Max Force, Min Pressure, User Notes, Last Time Ran, "))
        self.backButton.setText(_translate("FileStartWidget", "Back"))
        self.startButton.setText(_translate("FileStartWidget", "START"))

    def updateScreen(self, filePath):
        _translate = QtCore.QCoreApplication.translate
        self.file = FileLoader.PresetFile(filePath)
        self.presetName.setText(_translate("FileStartWidget", self.file.getName()))
        
        setStr = ("File Details:\n" + str(self.file.getDetails()) + 
        "\nRun Time (hr:min:sec):\n" + str(self.file.getTimeRead()) + 
        "\nMax Temp:\n" + str(self.file.getMaxTemp()) + 
        " °C\nMax Force:\n{:,.0f}".format(self.file.getMaxForce()) +
        " N\nMin Pressure:\n" + str(self.file.getMinPressure()) + 
        " Pa\nLast Time Accessed:\n" + str(self.file.getLastAccess()))
        
        self.presetDetails.setText(_translate("FileStartWidget", setStr))
        self.a2 = pg.AxisItem("left")
        self.a3 = pg.AxisItem("left")

        self.v2 = pg.ViewBox()
        self.v3 = pg.ViewBox()

        #l = pg.GraphicsLayout()

        self.graphWidget.addItem(self.a2, row = 2, col = 2, rowspan=1, colspan=1)
        self.graphWidget.addItem(self.a3, row = 2, col = 1, rowspan=1, colspan=1)

        self.pI = pg.PlotItem()
        self.v1 = self.pI.vb
        self.graphWidget.addItem(self.pI, row = 2, col = 3, rowspan=1, colspan=1)

        self.graphWidget.scene().addItem(self.v2)
        self.graphWidget.scene().addItem(self.v3)

        self.a2.linkToView(self.v2)
        self.a3.linkToView(self.v3)
        
        self.v2.setXLink(self.v1)
        self.v3.setXLink(self.v2)

        self.pI.getAxis("left").setLabel('Force (N)', color='#FFFFFF')
        self.a2.setLabel('Pressure (pa)', color='#2EFEF7')
        self.a3.setLabel('Temperature (°C)', color='#FF0000')

        self.v1.addItem(pg.PlotCurveItem(self.file.getTimeLst(), self.file.getForceLst(), pen='#FFFFFF'))
        self.v2.addItem(pg.PlotCurveItem(self.file.getTimeLst(), self.file.getPressLst(101000), pen='#2EFEF7'))
        self.v3.addItem(pg.PlotCurveItem(self.file.getTimeLst(), self.file.getTempLst(20), pen='#FF0000'))

        self.v1.sigResized.connect(self.updateViews)

        self.v2.enableAutoRange(axis= pg.ViewBox.XYAxes, enable=True)
        self.v3.enableAutoRange(axis= pg.ViewBox.XYAxes, enable=True)

        self.updateViews()



        # self._plot(self.file.getTimeLst(), self.file.getForceLst(), "Force", 'g')
        # self._plot(self.file.getTimeLst(), self.file.getPressLst(), "Pressure", 'b')
        # self._plot(self.file.getTimeLst(), self.file.getTempLst(101000), "Temperature", 'r')


    def _plot(self, x, y, plotName, colour):
        pen = pg.mkPen(color=colour)
        self.graphWidget.plot(x, y, name=plotName, pen=pen, symbol='+', symbolSize=30, symbolBrush=(colour))

    def updateViews(self):
        self.v2.setGeometry(self.v1.sceneBoundingRect())
        self.v3.setGeometry(self.v1.sceneBoundingRect())

    def switch(self, switchTo):
        self.switch_window.emit(switchTo)

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # controller = Controller()
    # controller.show_login()
    # sys.exit(app.exec_())
    
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_FileStartWidget()
    win.updateScreen('GUI_PyQt_Combined/Presets/test1.csv')

    win.show()
    sys.exit(app.exec_())