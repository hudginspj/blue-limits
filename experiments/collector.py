
MIN_WINDOWS = 10
WINDOW_SIZE = 10


class Collector(object):


    # The class "constructor" - It's actually an initializer 
    def __init__(self):
        self.columns = 5
        self.points = []
        self.counter = -1

    def addPoint(self, point):
        self.points.append(point)
        self.counter += 1

    def nextXWindow(self):
        if self.counter >= WINDOW_SIZE + 1:
            ret = []
            for i in range(WINDOW_SIZE):
                point = self.points[self.counter - i - 1]
                ret.append(point[0])
            return ret
        else:
            return None

    def nextYOutputs(self):
        if self.counter >= WINDOW_SIZE + 1:
            return [self.points[self.counter][0]]
        else:
            return None



if __name__ == "__main__":
    c = Collector()
    for i in range(100):
        c.addPoint([i])
    print(c.nextXWindow())
    print(c.nextYOutputs())






