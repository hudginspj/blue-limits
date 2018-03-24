import collectorv3

a_counter = 0

def addAnomaly(point):
    global a_counter
    a_counter += 1
    mod = a_counter % 80
    dif = 0
    if (mod > 60):
        dif = (mod - 60) * 0.1
    point[1]['temp'] += dif 


















