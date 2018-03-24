import collector
import xRegresor

NUM_TRAINING_POINTS = 100
training_points = [] #structures
training_windows = [] #numpy arrays
training_outputs = []

simData = None #TODO
collector = Collector()
for i in range(NUM_TRAINING_POINTS):
    point = simData.nextPoint()
    collector.addPoint(point)
    window = collector.nextXWindow()
    if window:
        training_windows.append(window)
        training_outputs.append(collector.nextYOutputs)
    
    regressor = xRegressor.Regressor()
    regressor.train(training_windows, training_outputs)



# Next do the predictions











