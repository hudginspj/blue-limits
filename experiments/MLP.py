import numpy as np, math, pandas as pds
from sklearn import cross_validation, preprocessing,svm


def regressor(**teledata):
    dataframe = pds.DataFrame(columns=('Mode','OrbitAngle','Temperature','Battery'))
    dataframe = dataframe.append({'Mode':teledata['Mode'],'OrbitAngle','Temperature','Battery'})





