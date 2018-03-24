
import matplotlib.pyplot as plt
from matplotlib import style
style.use("dark_background")



def graph(timestamps, realValues, predictedValues):
    plt.plot(timestamps, realValues, 'b')
    plt.plot(timestamps, predictedValues, 'r')
    plt.show()
    

