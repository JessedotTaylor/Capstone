from conversions import *
import math
import matplotlib.pyplot as plt

Al_6061_T6 = {
    'Outgassing Rate' : 2.5e-9 # Torr * L / sec *cm^2
}

# Al_6063
ATM = 101325

class Chamber():
    def __init__(self, l, w, h, material):
        
        dimensions = []
        for dimension in [l,w,h]:
            if dimension > 100: # Assuming dimension in mm
                dimensions.append(mm2m(dimension)) 
            elif 10 < dimension < 100: #Assuming dimension in cm
                dimensions.append(cm2m(dimension))
            else:   # Assuming dimension in m
                dimensions.append(dimension)
        
        self.l, self.w, self.h = dimensions
        self.material = material    

        self.Volume = self.l * self.w * self.h # m^3
        self.SurfaceArea = 2*self.l*self.h + 2*self.l*self.w + 2*self.w*self.h # m^2

    

    def gasIn(self, time): # material, time(sec) returns L
        surfaceAreaSquareM = self.SurfaceArea
        surfaceAreaSquareCM = squareM2squareCM(surfaceAreaSquareM)

        gasIn = self.material['Outgassing Rate'] * time * surfaceAreaSquareCM # Torr * L
        return Torr2Pa(gasIn) # L

    def getMaxL(self):
        return cubicM2L(self.Volume)

def pumpPerformace(currentL, maxL, verbose=False): # Returns pump performance between 0 and 1 
    performance = 1 - maxL ** -(currentL / maxL) 
    if verbose:
        print("Pump Performance - Current L: {:.3f}L, Max L: {:.3f}L, Performance: {:.3f}".format(currentL, maxL, performance))
    return performance

def currentL(time, step, maxL, maxFlow, verbose=False):
    if time > 0:
        alreadyRemoved = currentL(time-step, step, maxL, maxFlow)
        stepRemove = maxFlow * pumpPerformace(maxL - alreadyRemoved, maxL)
        if verbose:
            print("currentL - Removed this step: {:.6f}L, Already Removed: {:.6f} L".format(stepRemove, alreadyRemoved))
        return stepRemove + alreadyRemoved
    else:
        return 0.0


def stepL(time, step, ch, maxFlow, verbose=False):
    maxL = ch.getMaxL() # L
    if time > 0:
        gasIn = ch.gasIn(time)
        subL = currentL(time, step, maxL, maxFlow)
        currL = maxL  - subL + gasIn
        if verbose:
            print("stepL - time: {:.1f}s, Current L: {:.3f} L, Gas out: {:.3f} L, Gas In: {:.6f} L".format(time, currL, subL, gasIn))

        return currL
    else:
        return maxL


#Pump flow rate = 70 L / min
ch = Chamber(265, 265, 350, Al_6061_T6)
# ch = Chamber(.265, .265, .350, Al_6061_T6)
precision = 1
end_time = 60 #s
verbose = False
if verbose:
    print("Max Chamber L: {:,.3f} L".format(ch.getMaxL()))

timeLst = []
resLst = []
for time in range(int(end_time * precision)):
    time = time / precision
    timeLst.append(time)
    chambL = stepL(time, 1/precision, ch, 70/60/precision)
    resLst.append(chambL)
    if verbose:
        print("Core Loop - time: {:.1f}s, Chamber L: {:,.3f} L".format(time, chambL))

print("Air in Chamber @ t = {:.1f}s : {:,.3f} L".format(time, chambL))
plt.plot(timeLst, resLst)
plt.ylabel('Air in Chamber (L)')
plt.xlabel("Time (s)")
plt.show()




