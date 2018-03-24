import random
import math

counter = 0

def nextPoint():
    global counter
    counter += 1
    time = float(counter)
    mode = random.randrange(5)
    orbitAngle = 2.0 *  math.pi * (counter % 100) / 100.0
    temp = math.sin(orbitAngle)
    point = (time, {"mode": mode, "orbitAngle": orbitAngle, "temp": temp})
    return point


if __name__ == "__main__":
    print(nextPoint())