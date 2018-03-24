import collectorv3 as col
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import xSimData as simData
import xRegressor
import rangeCalc
import liveMonitor
import time
import simAnomaly2
import cosmosServer


####################### Train for predictions ####################
print("Training for predictions")

NUM_TRAINING_POINTS = 100
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

regressor = xRegressor.Regressor(1)
regressor.train(training_windows, training_outputs)

####################### Train for ranges ####################

print("Training for ranges")
training_points = []
training_windows = [] 
training_outputs = []

for i in range(NUM_TRAINING_POINTS):
    point = simData.nextPoint()
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        training_windows.append(window)
        training_outputs.append(collector.nextYOutputs())

ranger = rangeCalc.Ranger(1)
ranger.train(training_windows, training_outputs)


########### Run live ####################

print("Running live")
monitor = liveMonitor.LiveMonitor(1)
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
    print(e)


# NUM_test_POINTS = 100
# testing_points = []  # structures
# testing_windows = []  # numpy arrays
# testing_outputs = []
# timestamps=[]
# real_values=[]
# predictions = []

# for i in range(NUM_test_POINTS):
#     point = xSimData.nextPoint()
#     timestamps.append(point[0])
#     real_values.append(point[1]["temp"])
#     collector.addPoint(point)
#     window = collector.nextXWindow()
#     if window:
#         prediction = regressor.predict(window)[0]
#         predictions.append(prediction)
#         # test_windows.append(window)
#         # test_outputs.append(collector.nextYOutputs)
