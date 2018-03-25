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
    # fig2 = fig.add_subplot(2, 3, 2)
    # fig3 = fig.add_subplot(2, 3, 3)
    fig4 = fig.add_subplot(2, 1, 2)
    font_dict = {'family': 'serif',
                 'color': 'green',
                 'size': 15}

    def graph(timestamps, realValues, predictedValues, b1, b2, anomaly=False, lm1=2.1, lm2=-2.1, redll=-2.4, redlh=2.4):
        cnter = 1
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
        fig1.plot(timestamps, lm1s, 'yellow')
        fig1.plot(timestamps, lm2s, 'yellow')
        fig1.plot(timestamps, lreds, 'red')
        fig1.plot(timestamps, hreds, 'red')
        fig1.plot(timestamps, predictedValues, 'xkcd:green', label="Preds")
        fig1.plot(timestamps, realValues, 'orange', label="Reals")
        fig1.plot(timestamps, b1, 'blue', label="Bound1")
        fig1.plot(timestamps, b2, 'blue', label="Bound2")


        fig1.set_title('Temperature', font_dict)
        # plt.legend()
        # fig1.get_legend()
        if anomaly:
            plt.set_title('Anomaly', font_dict)
            plt.annotate('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(color='darkred'))
            # plt.draw()
        else:
            pass
        plt.pause(0.01)
        # pic = fig1.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
        # fig.savefig('ax2_figure.png', bbox_inches=pic)
        cnter +=1
    def orbitangleplot(timestamp, orbitangle):
        fig2.plot(timestamp, orbitangle)
        fig2.set_title('Orbit Angle', font_dict)
        plt.pause(0.01)
    def accelxplot(timestamps, accelx):
        fig3.plot(timestamps, accelx, 'red')
        fig3.set_title('Acceleration', font_dict)
        plt.pause(0.01)

    def modes(timestamps, modes):
        fig4.plot(timestamps, modes, 'orange')
        fig4.set_title('Modes', font_dict)
        plt.pause(0.01)

    # plt.legend()
    # fig1.get_legend()
    plt.show()


except Exception as e:
    print(e)



