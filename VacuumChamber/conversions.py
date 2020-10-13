def TorrLpS2PaM3pS(TorrLpS):
    return 7.5 * TorrLpS

def L2cubicM(liter):
    return liter / 1000

def cubicM2L(cubicM):
    return cubicM * 1000

def mm2m(mm):
    return mm / 1000

def cm2m(cm):
    return cm / 100

def squareCM2squareM(squareCM):
    return squareCM / 10000

def squareM2squareCM(squareM):
    return squareM * 10000

def Torr2Pa(Torr):
    return Torr * 133.322

def pressure(currL, maxL):
    return currL / maxL

def pressurePa(currL, maxL):
    return pressure(currL, maxL) * 101325

def pressureAtm(currL, maxL):
    return pressurePa(currL, maxL) / 101325

