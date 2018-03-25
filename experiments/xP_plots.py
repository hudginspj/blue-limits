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
    fig1 = fig.add_subplot(2, 1, 1)
    fig2 = fig.add_subplot(2, 1, 2)

    def graph(timestamps, realValues, predictedValues, b1, b2, anomaly=False, lm1=1.6, lm2=-1.6):
        cnter = 1
        lm1s = []
        lm2s = []
        for i in range(timestamps.__len__()):
            lm1s.append(lm1)
        for i in range(timestamps.__len__()):
            lm2s.append(lm2)
        fig1.plot(timestamps, lm1s, 'yellow')
        fig1.plot(timestamps, lm2s, 'yellow')
        fig1.plot(timestamps, realValues, 'orange')
        fig1.plot(timestamps, b1, 'blue')
        fig1.plot(timestamps, b2, 'blue')
        fig1.plot(timestamps, predictedValues, 'xkcd:green')
        if anomaly:
            font_dict = {'family': 'serif',
                         'color': 'darkred',
                         'size': 15}
            fig1.title('Anomaly', font_dict)
            fig1.annotate('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(color='darkred'))
            # plt.draw()
        else:
            pass
        plt.pause(0.01)
        plt.savefig(str(cnter)+'.png')
        plt.pause(0.01)
        cnter +=1
    def modes(timestamps, modes):
        fig2.plot(timestamps, modes, 'orange')
        plt.pause(0.01)

    plt.show()

except Exception as e:
    print(e)



