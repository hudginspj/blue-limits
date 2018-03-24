import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy
import matplotlib.pyplot as plt
import collectorv3 as col
import xP_plots


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
        if self.counter > 0 and (self.counter % 50) == 0:
            self.plotRange(50, 'temp')


        


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
        xP_plots.graph(times, reals, preds, upper_bounds, lower_bounds)
        print("times", times)

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








