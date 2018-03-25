import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy
import matplotlib.pyplot as plt
import collectorv3 as col
import xP_plots
import popupplots


PLOT_CONSTANTLY = False

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
        # print(point)
        # print(pointRanges)
        self.counter += 1
        self.points.append(point)
        for k in pointPredictions.keys():
            self.predictionsDict[k].append(pointPredictions[k])
            self.rangesDict[k].append(pointRanges[k])
        self.cosmosPlot(point)
        if PLOT_CONSTANTLY:
            if self.counter > 0 and (self.counter % 50) == 0:
                self.plotRange(50, 'TEMP2')
        else:
            anomalyKey = self.detectAnomalyKey(point, pointPredictions, pointRanges)
            if anomalyKey:
                self.plotRange(50, anomalyKey, True)




    def detectAnomalyKey(self, point, pointPredictions, pointRanges): #returns key of anomaly if exists
        # if self.counter > 0 and (self.counter % 50) == 0:
        #     return 'temp'
        for k in pointPredictions.keys():
            upper = pointPredictions[k] + pointRanges[k]
            lower = pointPredictions[k] - pointRanges[k]
            if point[1][k] > upper or point[1][k] < lower:
                if self.counter % 10 == 0:
                    return 'temp'
        return None




    def plotRange(self, num_points, variable, anomaly=False):
        times = [p[0] for p in self.points[-num_points:]]
        reals = [p[1][variable] for p in self.points[-num_points:]]
        # angles = [p[1]['orbitAngle'] for p in self.points[-num_points:]]
        # accelx = [p[1]['ACCELX'] for p in self.points[-num_points:]]
        modes = [p[1]['mode'] for p in self.points[-num_points:]]
        preds = self.predictionsDict[variable][-num_points:]
        ranges = self.rangesDict[variable][-num_points:]
        # print("times", times)
        # print("preds ", preds)
        # print("reals", reals)
        upper_bounds = [preds[i] + ranges[i] for i in range(num_points)]
        lower_bounds = [preds[i] - ranges[i] for i in range(num_points)]
        if PLOT_CONSTANTLY:
            xP_plots.graph(times, reals, preds, upper_bounds, lower_bounds, anomaly)
            # xP_plots.orbitangleplot(times, angles)
            # xP_plots.accelxplot(times, accelx)
            xP_plots.modes(times, modes)
            # print("times", times)
        else:
            popupplots.graph(times, reals, preds, upper_bounds, lower_bounds, anomaly)
            # xP_plots.modes(times, modes)

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








