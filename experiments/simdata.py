# point = (timestamp{var:value})
# temp - sine curve 
# orbit - radians in a circle
# mode- random int
import numpy as np 
import random
import matplotlib.pyplot as plt
import pandas as pd
from math import cos,sin,pi,sqrt
from scipy.stats import norm


counter = 0
mode = 0

def nextPoint():
    global counter
    counter += 1
    time = float(counter)
    mode = nextMode()
    orbitAngle = 2.0 *  pi * (counter % 100) / 100.0
    temp = sin(orbitAngle)
    temp2 = cos(orbitAngle)
    point = (time, {"mode": mode, 
        "orbitAngle": orbitAngle, 
        "temp": temp, 
        "TEMP2": tempf(orbitAngle),
        "ACCELX": nextAccel()
    })

    return point

def nextMode():
    global mode
    if random.randrange(10) == 0:
        mode = random.randrange(3)
    return mode

def nextAccel():
    if mode == 1:
        return random.uniform(-2.0, 2.0)
    else:
        return random.uniform(-0.1, 0.1)

def tempf(angle):
    return abs(sin(2*angle) + sin(angle)) 
    #return sin(.0625sin(angle)+sin(angle%90))
    #return TAYLOR SERIES GOES HERE
    #return sin(2*angle) + sin(angle)

if __name__ == "__main__":
    print(nextPoint())

lastAccel = 0.0

def nextAccel():
    global lastAccel
    
    if mode == 1:
        return random.uniform(-2.0, 2.0)
    else:
        return random.uniform(-0.1, 0.1)

def nextAccelWalk():
    global lastAccel
    upper = 0.1
    lower = -0.1
    if mode == 1:
       upper = 2.0
       lower = -2.0

    maxStep = upper / 4.0
    lastAccel += random.uniform(-maxStep, maxStep)

    if lastAccel > upper:
        lastAccel = upper
    if lastAccel < lower:
        lastAccel = lower
    
    return lastAccel






# def accel_x():

# def other_period():

# def normiedata():
#     x = np.linspace(0, 1000, 100)
#     y = (2*x) + np.random.randn(5)
#     data = np.hstack((x.reshape(100,1), y.reshape(100,1)))
#     return

# def triangle(counter, amplitude):
#      counter += 1
#      for direction in (1, -1):
#          for i in range():
#              yield i * (amplitude / section) * direction
#          for i in range(section):
#              yield (amplitude - (i * (amplitude / section))) * direction


########################
# Testing code below 
########################

# counter = 0

# def nextPoint():
#     counter += 1
#     time = float(counter)
#     mode = random.randrange(5)
#     orbitAngle = 2.0 *  math.pi * (counter % 100) / 100.0
#     temp = math.sin(orbitAngle)
#     point = (time, {"mode": mode, "orbitAngle": orbitAngle, "temp": temp})
#     return point


# def point_on_circle():
#     '''
#         Finding the x,y coordinates on circle, based on given angle
#     '''
#     from math import cos, sin, pi
#     #center of circle, angle in degree and radius of circle
#     center = [0,0]
#     angle = pi / 2
#     radius = 100
#     x = center[0] + (radius * cos(angle))
#     y = center[1] + (radius * sin(angle))

#     return x,y



# from itertools import islice

# def window(seq, n=2):
#     "Returns a sliding window (of width n) over data from the iterable"
#     "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
#     it = iter(seq)
#     result = tuple(islice(it, n))
#     if len(result) == n:
#         yield result
#     for elem in it:
#         result = result[1:] + (elem,)
#         yield result


# def window(seq, n=2):
#     it = iter(seq)
#     win = deque((next(it, None) for _ in xrange(n)), maxlen=n)
#     yield win
#     append = win.append
#     for e in it:
#         append(e)
#         yield win

# def brownian(x0, n, dt, delta, out=None):
#     """
#     Generate an instance of Brownian motion (i.e. the Wiener process):

#         X(t) = X(0) + N(0, delta**2 * t; 0, t)

#     where N(a,b; t0, t1) is a normally distributed random variable with mean a and
#     variance b.  The parameters t0 and t1 make explicit the statistical
#     independence of N on different time intervals; that is, if [t0, t1) and
#     [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
#     are independent.
    
#     Written as an iteration scheme,

#         X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)


#     If `x0` is an array (or array-like), each value in `x0` is treated as
#     an initial condition, and the value returned is a numpy array with one
#     more dimension than `x0`.

#     Arguments
#     ---------
#     x0 : float or numpy array (or something that can be converted to a numpy array
#          using numpy.asarray(x0)).
#         The initial condition(s) (i.e. position(s)) of the Brownian motion.
#     n : int
#         The number of steps to take.
#     dt : float
#         The time step.
#     delta : float
#         delta determines the "speed" of the Brownian motion.  The random variable
#         of the position at time t, X(t), has a normal distribution whose mean is
#         the position at time t=0 and whose variance is delta**2*t.
#     out : numpy array or None
#         If `out` is not None, it specifies the array in which to put the
#         result.  If `out` is None, a new numpy array is created and returned.

#     Returns
#     -------
#     A numpy array of floats with shape `x0.shape + (n,)`.
    
#     Note that the initial value `x0` is not included in the returned array.
#     """

#     x0 = np.asarray(x0)

#     # For each element of x0, generate a sample of n numbers from a
#     # normal distribution.
#     r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))

#     # If `out` was not given, create an output array.
#     if out is None:
#         out = np.empty(r.shape)

#     # This computes the Brownian motion by forming the cumulative sum of
#     # the random samples. 
#     np.cumsum(r, axis=-1, out=out)

#     # Add the initial condition.
#     out += np.expand_dims(x0, axis=-1)

#     return out


