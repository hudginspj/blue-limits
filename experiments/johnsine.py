import matplotlib.pyplot as plt
import numpy as np
import random as rnd

def temp_periodic():
    global counter
    time = float(counter)
    mode = rnd.randrange(2)
    Fs=8000
    freq=250
    while True:
        counter += 1
        x = np.arange(time)
        orbitAngle = np.sin(2 * np.pi * freq * time % 200 / Fs)
        temp = orbitAngle
        point = (time, {"mode": mode, "orbitAngle": orbitAngle, "temp": temp})
    plt.scatter(x,temp)
    plt.show()
    plt.xlabel("XLABEL")
    plt.ylabel("YLABEL")
    return point

#if __name__ == "__main__":
#    print(temp_periodic())
    

# def accel_period():
#     Fs=8000
#     f=250
#     counter = 0
#     while True:
#         counter += 1
#         x = np.arange(counter)
#         y = np.sin(2 * np.pi * f * x / Fs)
#     plt.scatter(x,y)
#     plt.show()
#     plt.xlabel("XLABEL")
#     plt.ylabel("YLABEL")
#     return

# def sine1():
#     Fs=8000
#     f=250
#     counter = 0
#     while True:
#         counter += 1
#         x = np.arange(counter)
#         y = np.sin(2 * np.pi * f * x / Fs)
#     plt.scatter(x,y)
#     plt.show()
#     plt.xlabel("XLABEL")
#     plt.ylabel("YLABEL")
#     return



# def normiedata():
#     x = np.linspace(0, 1000, 100)
#     y = (2*x) + 2 + 20*np.random.randn(100)
#     data = np.hstack((x.reshape(100,1), y.reshape(100,1)))
#     return