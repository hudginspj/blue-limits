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
    fig1 = fig.add_subplot(2, 3, 1)
    fig2 = fig.add_subplot(2, 3, 2)
    fig3 = fig.add_subplot(2, 3, 3)
    fig4 = fig.add_subplot(2, 1, 2)
    font_dict = {'family': 'serif',
                 'color': 'green',
                 'size': 8}

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

        fig1.set_title('Temp Learn Curve', font_dict)
        if anomaly:
            fig1.set_title('Anomaly', font_dict)
            fig1.__annotations__('',(timestamps[len(timestamps)-1],realValues[len(realValues)-1]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(color='darkred'))
            # plt.draw()
        else:
            pass
        plt.pause(0.01)
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


    plt.show()


except Exception as e:
    print(e)



