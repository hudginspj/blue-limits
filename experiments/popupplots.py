from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from matplotlib import style
import  numpy as np
import matplotlib.animation as animation
style.use("dark_background")

try:
    plt.ion()
    fig = plt.figure()
    font_dict = {'family': 'serif',
                 'color': 'green',
                 'size': 15}

    def graph(timestamps, realValues, predictedValues, b1, b2, anomaly=False, lm1=2.1, lm2=-2.1, redll=-2.4, redlh=2.4):
        if anomaly:
            plt.clf()
            # cnter = 1
            lm1s = []
            lm2s = []
            lreds = []
            hreds = []
            for i in range(timestamps.__len__()):
                lm1s.append(lm1)
            for i in range(timestamps.__len__()):
                lm2s.append(lm2)
            for i in range(timestamps.__len__()):
                lreds.append(redll)
            for i in range(timestamps.__len__()):
                hreds.append(redlh)
            plt.plot(timestamps, lm1s, 'yellow')
            plt.plot(timestamps, lm2s, 'yellow')
            plt.plot(timestamps, lreds, 'red')
            plt.plot(timestamps, hreds, 'red')
            plt.plot(timestamps, predictedValues, 'xkcd:green', label="Preds")
            plt.plot(timestamps, realValues, 'orange', label="Reals")
            plt.plot(timestamps, b1, 'blue', label="Bound1")
            plt.plot(timestamps, b2, 'blue', label="Bound2")
            plt.title('Anomaly', font_dict)
            plt.annotate('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                         xytext=(0.8, 0.9), textcoords='axes fraction',
                         arrowprops = dict(color='darkred'))
            plt.pause(0.01)
        else:
            plt.clf()
            # cnter = 1
            lm1s = []
            lm2s = []
            lreds = []
            hreds = []
            for i in range(timestamps.__len__()):
                lm1s.append(lm1)
            for i in range(timestamps.__len__()):
                lm2s.append(lm2)
            for i in range(timestamps.__len__()):
                lreds.append(redll)
            for i in range(timestamps.__len__()):
                hreds.append(redlh)
            plt.plot(timestamps, lm1s, 'yellow')
            plt.plot(timestamps, lm2s, 'yellow')
            plt.plot(timestamps, lreds, 'red')
            plt.plot(timestamps, hreds, 'red')
            plt.plot(timestamps, predictedValues, 'xkcd:green', label="Preds")
            plt.plot(timestamps, realValues, 'orange', label="Reals")
            plt.plot(timestamps, b1, 'blue', label="Bound1")
            plt.plot(timestamps, b2, 'blue', label="Bound2")
            plt.title('Temperature', font_dict)
            plt.pause(0.01)

            # fig1.get_legend()
        # if anomaly:
        #     plt.title('Anomaly', font_dict)
        #     plt.annotate('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
        #          xytext=(0.8, 0.9), textcoords='axes fraction',
        #          arrowprops = dict(color='darkred'))
        #     plt.draw()
        #     plt.pause(0.01)
        # else:
        #     pass
        # plt.pause(0.01)
        # pic = fig1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        # fig.savefig('ax2_figure.png', bbox_inches=pic)
        # cnter +=1

    # plt.show()


except Exception as e:
    print(e)



