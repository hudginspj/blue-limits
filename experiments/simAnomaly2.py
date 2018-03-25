import collectorv3

a_counter = 0

def addAnomaly(point):
    global a_counter
    a_counter += 1
    mod = a_counter % 120
    dif = 0
    if (mod > 60 and mod <=80):
        dif = (mod - 60) * 0.2
    point[1]['ACCELX'] += dif 


















