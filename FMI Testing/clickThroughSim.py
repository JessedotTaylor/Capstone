from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave
from fmpy.util import plot_result, download_test_file

from PyQt5 import QtWidgets
from pyqtgraph import PlotWidget, plot
from PyQt5 import QtCore
import pyqtgraph as pg

import numpy as np
import sys  # We need sys so that we can pass argv to QApplication
import os


def simulateCustomInputStep(fmu, time, inputs, stepSize, vrOutputs):
    # set the input
    fmu.setReal(inputs[0], inputs[1])

    # perform 1 step
    fmu.doStep(currentCommunicationPoint=time, communicationStepSize=stepSize)

    # get the values for 'inputs' and 'outputs'
    inputsRet, outputs = fmu.getReal([inputs[0], vrOutputs])
    return inputsRet, outputs

def startFmu(filename,
            startTime=0.0,
            threshold=2.0,
            stopTime=30.0,
            stepSize=None,
            ):
    
    if stepSize == None:
        stepSize = (stopTime - startTime) / 500

    modelDescription = read_model_description(filename)

    vrs = {}
    for variable in modelDescription.modelVariables:
        vrs[variable.name] = variable.valueReference

    # get the value references for the variables we want to get/set
    vrInputs = vrs['u'] # These need to be changed per model, or use standardised naming conventions
    vrOutputs = vrs['y']

    unzipdir = extract(filename)

    fmu = FMU2Slave(guid=modelDescription.guid,
                    unzipDirectory=unzipdir,
                    modelIdentifier=modelDescription.coSimulation.modelIdentifier,
                    instanceName='instance1') 

    # initalize
    fmu.instantiate()
    fmu.setupExperiment(startTime=startTime)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    return fmu, vrInputs, vrOutputs, startTime, stepSize, stopTime

def stopFmu(fmu):
    fmu.terminate()
    fmu.freeInstance()

def simulateCustomInput(filename, showPlot=True):

    # define the model name and simulation parameters
    startTime = 0.0
    threshold = 2.0
    stopTime = 30.0
    stepSize = (stopTime - startTime) / 500

    # read the model description
    modelDescription = read_model_description(filename)

    # collect the value references
    vrs = {}
    for variable in modelDescription.modelVariables:
        vrs[variable.name] = variable.valueReference

    # get the value references for the variables we want to get/set
    vrInputs = vrs['u'] # These need to be changed per model, or use standardised naming conventions
    vrOutputs = vrs['y']

    unzipdir = extract(filename)

    fmu = FMU2Slave(guid=modelDescription.guid,
                    unzipDirectory=unzipdir,
                    modelIdentifier=modelDescription.coSimulation.modelIdentifier,
                    instanceName='instance1') 

    # initalize
    fmu.instantiate()
    fmu.setupExperiment(startTime=startTime)
    fmu.enterInitializationMode()
    fmu.exitInitializationMode()

    time = startTime

    rows =[]

    # Sim loop
    while time < stopTime:

        # NOTE: the FMU.get*() and FMU.set*() functions take lists of
        # value references as arguments and return lists of values

        # set the input
        fmu.setReal([vrInputs], [0.0 if time < 1.0 else 1.0])

        # perform 1 step
        fmu.doStep(currentCommunicationPoint=time, communicationStepSize=stepSize)

        # get the values for 'inputs' and 'outputs'
        inputs, outputs = fmu.getReal([vrInputs, vrOutputs])

        # Use threshold to terminate sim
        if outputs > threshold:
            print("Threshold reached at t = {:.3f} s".format(time))
            break

        # append the results
        rows.append((time, inputs, outputs))

        # advance the time
        time += stepSize

    fmu.terminate()
    fmu.freeInstance()

    result = np.array(rows, dtype=np.dtype([('time', np.float64), ('inputs', np.float64), ('outputs', np.float64)]))

    if showPlot:
        plot_result(result)

    return time

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.fmu, self.vrInputs, self.vrOutputs, self.startTime, self.stepSize, self.stopTime = startFmu('FeedBack/FeedBack.fmu')
        self.currTime = 0

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = [0]
        self.y = [0]

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))

        # plot data: x, y values
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)
        #self.graphWidget.plot(hour, temperature)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.stepSize) #msec
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        # print("updatePlotData called: {:.2f}".format(self.currTime))
        if self.currTime < self.stopTime:
             # set the input
            self.fmu.setReal([self.vrInputs], [0.0 if self.currTime < 1.0 else 1.0])

            # perform 1 step
            self.fmu.doStep(currentCommunicationPoint=self.currTime, communicationStepSize=self.stepSize)

            # get the values for 'inputs' and 'outputs'
            inputs, outputs = self.fmu.getReal([self.vrInputs, self.vrOutputs])

            #self.x = self.x[1:]
            self.x.append(self.currTime)

            #self.y = self.y[1:]
            self.y.append(outputs)

            self.data_line.setData(self.x, self.y)

            self.currTime += self.stepSize
        
        else:
            self.timer.stop()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

    
    # simulateCustomInput('FMI Testing/FeedBack.fmu')


