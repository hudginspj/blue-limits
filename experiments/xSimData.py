import random
import math

counter = 0
mode = 0

def nextPoint():
    global counter
    counter += 1
    time = float(counter)
    mode = nextMode()
    orbitAngle = 2.0 *  math.pi * (counter % 100) / 100.0
    temp = math.sin(orbitAngle)
    temp2 = math.cos(orbitAngle)
    point = (time, {"mode": mode, 
        "orbitAngle": orbitAngle, 
        "temp": temp, 
        "TEMP2": temp2,
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


if __name__ == "__main__":
    print(nextPoint())