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

    def mode(timestamps, modes):
        plt.plot(timestamps, modes, 'crimson')
        plt.pause(0.01)
    plt.show()

except Exception as e:
    print(e)