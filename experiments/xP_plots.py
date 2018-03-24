from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib import style
import  numpy as np
import matplotlib.animation as animation
style.use("dark_background")

try:
    plt.ion()
    fig = plt.figure()
    clr = fig.add_subplot(1,1,1)

    def graph(timestamps, realValues, predictedValues, b1, b2, anomaly=False, lm1=1.6, lm2=-1.6):
        cnter = 1
        plt.plot(timestamps,, 'gold')
        plt.plot(timestamps,lm2[0], 'darkorange')
        plt.plot(timestamps, realValues, 'b')
        plt.plot(timestamps, b1, 'darkblue')
        plt.plot(timestamps, b2, 'darkred')
        plt.plot(timestamps, predictedValues, 'xkcd:green')
        if anomaly:
            font_dict = {'family': 'serif',
                         'color': 'darkred',
                         'size': 15}
            plt.title('Anomaly', font_dict)
            plt.annotate('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(color='darkred'))
            # plt.draw()
        else:
            pass
        plt.pause(1)
        plt.pause(0.1)
        plt.savefig(str(cnter)+'.png')
        plt.pause(0.1)
        cnter = cnter +1
        plt.show()

except Exception as e:
    print(e)



