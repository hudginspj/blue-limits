
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")

try:
    plt.ion()
    def graph(timestamps, realValues, predictedValues, b1, b2):
        plt.plot(timestamps, realValues, 'b')
        plt.plot(timestamps, b1, 'xkcd:red')
        plt.plot(timestamps, b2, 'xkcd:red')
        plt.plot(timestamps, predictedValues, 'xkcd:green')
        plt.draw()
        plt.pause(5)   
    plt.show()
except Exception as e:
    pass


