import collectorv3 as col
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import simdata as simData
import xRegressor
import rangeCalc
import liveMonitor
import time
import simAnomaly2
import cosmosServer


####################### Train for predictions ####################
print("Training for predictions")

NUM_TRAINING_POINTS = 600
training_points = []  # structures
training_windows = []  # numpy arrays
training_outputs = []


collector = col.Collector()
for i in range(NUM_TRAINING_POINTS):
    point = simData.nextPoint()
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        training_windows.append(window)
        training_outputs.append(collector.nextYOutputs())
        

regressor = xRegressor.Regressor(3)
regressor.train(training_windows, training_outputs)

####################### Train for ranges ####################

print("Training for ranges")
training_points = []
training_windows = [] 
training_outputs = []
training_predictions = []

for i in range(NUM_TRAINING_POINTS):
    point = simData.nextPoint()
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        training_windows.append(window)
        training_outputs.append(collector.nextYOutputs())
        training_predictions.append(regressor.predict(window))

ranger = rangeCalc.Ranger(3)
ranger.train(training_windows, training_outputs, training_predictions)


########### Run live ####################

print("Running live")
monitor = liveMonitor.LiveMonitor(3)
try:
    while True:
        time.sleep(0.1)
        point = simData.nextPoint()

        simAnomaly2.addAnomaly(point)

        cosmosServer.nextPoint = point
        collector.addPoint(point)
        window = collector.nextXWindow()
        if window:
            pointPredictions = col.outputsToDict(regressor.predict(window))
            pointRanges = col.outputsToDict(ranger.calcRanges(window))
            monitor.handleNext(point, pointPredictions, pointRanges)
except Exception as e:
    raise e



