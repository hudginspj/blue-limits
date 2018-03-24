import collectorv2
import xRegressor
import xSimData

NUM_TRAINING_POINTS = 100
training_points = [] #structures
training_windows = [] #numpy arrays
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



# Next do the predictions











