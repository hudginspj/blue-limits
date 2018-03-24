import collectorv2
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import xSimData
style.use("dark_background")
NUM_TRAINING_POINTS = 100
training_points = []  # structures
training_windows = []  # numpy arrays
training_outputs = []
graphxs=[]
graphys=[]

simData = None  # TODO
collector = collectorv2.Collector()
for i in range(NUM_TRAINING_POINTS):
    point = xSimData.nextPoint()
    graphxs.append(point[0])
    graphys.append(point[1]["temp"])
    # collector.addPoint(point)
    # window = collector.nextXWindow()
    # if window:
    #     training_windows.append(window)
    #     training_outputs.append(collector.nextYOutputs)
plt.plot(graphxs,graphys)
plt.show()

def graph(timestamps, realValues, predictedValues)

