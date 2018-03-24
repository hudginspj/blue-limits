import sklearn
from sklearn import datasets
# from sklearn import svm
import sklearn
from sklearn.ensemble import RandomForestRegressor
import numpy
import math
import matplotlib.pyplot as plt

# digits = datasets.load_digits()
# clf = svm.SVC(gamma=0.001, C=100.)
# clf.fit(digits.data[:-1], digits.target[:-1])
# print(clf.predict(digits.data[-1:]))



l = 100
ws = 10


sinx = numpy.array(range(l))
siny = numpy.array([math.sin(i) for i in range(l)])
# print(sinx, siny)
windows = numpy.zeros([l-ws, ws])
# print(windows)
target = numpy.zeros([l-ws])
for i in range(l-ws):
    for j in range(ws):
        windows[i][j] = siny[i+j]
        target[i] = siny[i+ws]



# clf = sklearn.svm.SVR(gamma=0.001, C=100.)
clf = RandomForestRegressor()
clf.fit(windows, target)
pred = clf.predict(windows[-10:])
print(pred)
print(target[-10:])


fig, ax = plt.subplots()
ax.plot(range(10), pred)
ax.plot(range(10), target[-10:])

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
ax.grid()

# fig.savefig("test.png")
plt.show()
