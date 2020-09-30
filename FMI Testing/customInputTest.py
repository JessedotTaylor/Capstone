from fmpy import read_model_description, extract
from fmpy.fmi2 import FMU2Slave
from fmpy.util import plot_result, download_test_file
import numpy as np
import shutil

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

if __name__ == "__main__":
    simulateCustomInput('FMI Testing/FeedBack.fmu')


