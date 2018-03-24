import numpy as np, math, pandas as pds
from sklearn import cross_validation, preprocessing,svm


dataframe = pds.DataFrame(columns=('Mode','OrbitAngle','Temperature','Battery'))
dataframe = np.array(dataframe.append(teledata))





