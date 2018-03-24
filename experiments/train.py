import collectorv2
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import xSimData
import xRegressor







NUM_TRAINING_POINTS = 100
training_points = []  # structures
training_windows = []  # numpy arrays
training_outputs = []


collector = collectorv2.Collector()
for i in range(NUM_TRAINING_POINTS):
    point = xSimData.nextPoint()
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        training_windows.append(window)
        training_outputs.append(collector.nextYOutputs())

regressor = xRegressor.Regressor(1)
regressor.train(training_windows, training_outputs)



NUM_test_POINTS = 100
testing_points = []  # structures
testing_windows = []  # numpy arrays
testing_outputs = []
timestamps=[]
real_values=[]
predictions = []



collector = collectorv2.Collector()
for i in range(NUM_test_POINTS):
    point = xSimData.nextPoint()
    timestamps.append(point[0])
    real_values.append(point[1]["temp"])
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        prediction = regressor.predict(window)[0]
        predictions.append(prediction)
        print("prediction", prediction)
        # test_windows.append(window)
        # test_outputs.append(collector.nextYOutputs)

# xP_plots.graph(timestamps, real_values, predictions)