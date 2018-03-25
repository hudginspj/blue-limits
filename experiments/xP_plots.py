
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.animation as animation
style.use("dark_background")

try:
    plt.ion()
    fig = plt.figure()
    clr = fig.add_subplot(1,1,1)
    def graph(timestamps, realValues, predictedValues, b1, b2, anomaly=False):
        # print("Anomaly: ", anomaly)
        clr.clear()
        plt.plot(timestamps, realValues, 'b')
        plt.plot(timestamps, b1, 'xkcd:red')
        plt.plot(timestamps, b2, 'xkcd:red')
        plt.plot(timestamps, predictedValues, 'xkcd:green')
        plt.draw()
        if anomaly:
            plt.annotate('Anomoly in temp',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(color='darkred'))
            # plt.draw()
        else:
            pass
        plt.draw()
        plt.pause(1)

    plt.show()
except Exception as e:
    pass


