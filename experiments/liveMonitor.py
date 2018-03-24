import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy
import collectorv3 as col

PLOT_CONSTANTLY = True

class LiveMonitor(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, num_outputs):
        self.num_outputs = num_outputs
        self.counter = -1
        self.points = []
        self.predictionsDict = {} # Dictionary of lists of predictions
        self.rangesDict = {} #Dictionary of lists of ranges
        emptyPoint = col.outputsToDict([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        for k in emptyPoint.keys():
            # print("key", k)
            self.predictionsDict[k] = []
            self.rangesDict[k] = []

    def handleNext(self, point, pointPredictions, pointRanges):
        # print("pointPredictions", pointPredictions)
        self.counter += 1
        self.points.append(point)
        for k in pointPredictions.keys():
            self.predictionsDict[k].append(pointPredictions[k])
            self.rangesDict[k].append(pointRanges[k])
        self.cosmosPlot(point)
        if PLOT_CONSTANTLY:
            if self.counter > 0 and (self.counter % 50) == 0:
                self.plotRange(50, 'temp')
        else:
            anomalyKey = self.detectAnomalyKey()
            if anomalyKey:
                self.plotRange(50, anomalyKey)



    def detectAnomalyKey(self, point, pointPredictions): #returns key of anomaly if exists
        if self.counter > 0 and (self.counter % 50) == 0:
            return 'temp'
        else
            return None



    def plotRange(self, num_points, variable):
        times = [p[0] for p in self.points[-num_points:]]
        reals = [p[1][variable] for p in self.points[-num_points:]]
        preds = self.predictionsDict[variable][-num_points:]
        ranges = self.rangesDict[variable][-num_points:]
        print("times", times)
        print("preds ", preds)
        print("ranges", ranges)
        upper_bounds = [preds[i] + ranges[i] for i in range(num_points)]
        lower_bounds = [preds[i] - ranges[i] for i in range(num_points)]
        print("times", times)
        #TODO graph(times, reals, preds, lower_bounds, upper_bounds)


    

    def ranges(self, xWindow):
        ranges = []
        for i_out in range(self.num_outputs):
            pass
            # prediction = self.regressors[i_out].predict(xWindow)
        return ranges

    def cosmosPlot(self, point):
        #col.pointToOutputs(point)
        pass #TODO

   

if __name__ == "__main__":
    print(nextPoint())








