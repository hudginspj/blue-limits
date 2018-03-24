import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy
import collectorv3 as col



class LiveMonitor(object):
    # The class "constructor" - It's actually an initializer 
    def __init__(self, num_outputs):
        self.num_outputs = num_outputs
        self.counter = -1
        self.points = []
        self.predictionsDict = [] # Dictionary of lists of predictions
        self.rangesDict = [] #Dictionary of lists of ranges

    def handleNext(self, point, pointPredictions, pointRanges):
        self.counter += 1
        #add to dicts
        self.cosmosPlot(point)
        if counter > 0 and (counter % 50):
            plotRange(50, 'temp')


    def emptyOutputDict(self):
        emptyPoint = col.outputsToDict([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
        for k in emptyPoint.keys():
            print("key", k)


    def plotRange(num_points, variable):
        times = [p[0] for p in points[-num_points:]]
        reals = [p[0][variable] for p in points[-num_points:]]
        preds = self.predictionsDict[variable][-num_points:]
        ranges = self.rangesDict[variable][-num_points:]
        upper_bounds = [preds[i] + ranges[i] for i in points]
        lower_bounds = [preds[i] - ranges[i] for i in points]
        #TODO plot(times, reals, preds, lower_bounds, upper_bounds)

    

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








