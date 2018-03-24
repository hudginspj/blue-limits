import numpy as np, math
from sklearn import cross_validation, preprocessing,svm
import xSimData
point = xSimData.nextPoint()

l = [point[1]['mode'], point[1]['orbitAngle'], point[1]['temp']]
for i in range(10):
    point = xSimData.nextPoint()
    l.append(point[1]['mode'])
    l.append(point[1]['orbitAngle'])
    l.append(point[1]['temp'])
array = np.array(l)
print(array)






