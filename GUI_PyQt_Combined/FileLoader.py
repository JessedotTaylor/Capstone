import os, datetime

class PresetFile:
    def __init__(self, pathToFile):
        self.lineDic = {}
        self.maxTemp = 0
        self.maxForce = 0
        self.runTimeS = 0
        self.minPressure = 99
        self.lastAccess = ''
        self.runTime = ''

        self.loadFile(pathToFile)

    def loadFile(self, pathToFile):
        with open(pathToFile, 'r') as f:            #NEEDS ERROR HANDLING
            lines = f.readlines()
        
        lenLines = len(lines)
        linePtr = 0
        while lines[linePtr].split(',')[0] != '':
            obj = lines[linePtr].split(',')
            if obj[2] != '':
                self.lineDic[str(obj[0])] = ','.join(obj[1:])
            else:
                self.lineDic[str(obj[0])] = str(obj[1])
            linePtr += 1
        
        linePtr += 1
        self.headers = [x.strip('\n') for x in lines[linePtr].split(',')]
        lenHeaders = len(self.headers)
        for header in self.headers:
            self.lineDic[header.strip('\n')] = []
        linePtr += 1

        while linePtr < lenLines:
            obj = lines[linePtr].split(',')
            for i in range(lenHeaders):
                if obj[i][0] != '~':
                    self.lineDic[self.headers[i]].append(float(obj[i]))
                else:
                    self.lineDic[self.headers[i]].append(obj[i].strip('\n'))
            linePtr += 1

        self.getMaxForce()
        self.getMaxTemp()
        self.getLastAccess(pathToFile)
        self.getTimeRead()


    def getLastAccess(self, pathToFile=None):
        #https://stackoverflow.com/questions/39359245/from-stat-st-mtime-to-datetime
        if self.lastAccess == '' and pathToFile != None:
            self.lastAccess = datetime.datetime.fromtimestamp(os.stat(pathToFile).st_atime)
        return self.lastAccess


    def getMaxTemp(self):
        if self.maxTemp == 0:
            self.maxTemp = self._getMax(self.getTempLst())
        return self.maxTemp
    
    def getMaxForce(self):
        if self.maxForce == 0: 
            self.maxForce = self._getMax(self.getForceLst())
        return self.maxForce

    def getMinPressure(self):
        if self.minPressure == 99:
            self.minPressure = self._getMin(self.getPressLst())
        return self.minPressure

    def _getMin(self, lst):
        currMin = 999999999999999999
        for x in lst:
            if x != '~' and x < currMin:
                currMin = x
        
        if currMin == 999999999999999999:
            return '~'
        return currMin
    
    def _getMax(self, lst):
        currMax = 0
        for x in lst:
            if x != '~' and x > currMax:
                currMax = x
        return currMax


    def getForceLst(self, rep=0):
        return [x if x != '~' else rep for x in self.lineDic['Force']]

    def getPressLst(self, rep=0):
        return [x if x != '~' else rep for x in self.lineDic['Press']]
    
    def getTempLst(self, rep=0):
        return [x if x != '~' else rep for x in self.lineDic['Temp']]
    
    def getTimeLst(self, rep=0):
        return [x if x != '~' else rep for x in self.lineDic['Time (min)']]
    
    def getName(self):
        return self.lineDic['Name']
    
    def getDetails(self):
        return self.lineDic['User Notes']
    
    def getTimeS(self):
        if self.runTimeS == 0:
            obj = self.lineDic['Run Time'].split(':')
            self.runTimeS = obj[0] * 60 * 60 + obj[1] * 60 + obj[2]
        return self.runTimeS
    
    def getTimeRead(self):
        if self.runTime == '':
            lst = self.getTimeLst()
            lastTime = lst[-1]
            hrs = str(int(lastTime // 60))
            mins = str(int(lastTime % 60))
            self.runTime = ':'.join([hrs, mins, '00'])
        return self.runTime

        
if __name__ == "__main__":
    PresetFile('GUI_PyQt_Combined/Presets/test1.csv')


