class elevator:

    def __init__(self, _id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime, src, dest, time) -> object:
        self._id = _id
        self.speed = speed
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.closeTime = closeTime
        self.openTime = openTime
        self.startTime = startTime
        self.stopTime = stopTime
        self.src = src
        self.dest = dest
        self.time = time

    def setSrc(self, src):
        self.src = src

    def setDest(self, dest):
        self.dest = dest

    def setTime(self, time):
        self.time = time

    def __calc__(self, call) -> int:
        timeSource = self.src
        ds1 = abs(self.dest - call.source)
        ds2 = abs(call.dest - call.source)
        computeTime = self.startTime + self.stopTime + self.openTime + self.closeTime
        timeOfWay = ds1 / self.speed + ds2 / self.speed + 2*computeTime - self.closeTime
        if self.time <= call.time:
            list = [timeOfWay, call.source, call.dest, timeOfWay + call.time]
            return list
        if self.time > call.time:
            # both of them are going up
            if call.ud & (self.dest - self.src) > 0:
                if self.src + abs(timeSource - call.time) * self.speed <= call.source:
                    # the call is inside the way of the elevator
                    if self.src <= call.source & call.dest <= self.dest:
                        curPosElev = self.src + self.speed * abs(call.time - timeSource)
                        timeOfWay = abs(call.dest - curPosElev) / self.speed + 2 * computeTime - self.startTime - self.closeTime
                        # list = [timeOfWay, call.source, self.dest, self.time + 2 * computeTime]
                        list = [timeOfWay, call.source, self.dest, call.time + timeOfWay]
                        return list
                    # the call src is inside and the dest is outside
                    if self.src <= call.source & call.dest >= self.dest:
                        curPosElev = self.src + self.speed * abs(call.time - timeSource)
                        timeOfWay = abs(call.dest - curPosElev) / self.speed + 2 * computeTime - self.startTime - self.closeTime
                        # list = [timeOfWay, call.source, call.dest, self.time + 2 * computeTime + (abs(call.dest - self.dest) / self.speed)]
                        list = [timeOfWay, call.source, call.dest, call.time + timeOfWay]
                        return list
                    # the call src and dest is outside
                    if call.src > self.dest & call.dest > self.dest:
                        timeOfWay = self.time + abs(call.dest - self.dest) / self.speed + 2 * computeTime
                        # list = [timeOfWay, call.source, call.dest, self.time + timeOfWay]
                        list = [timeOfWay, call.source, call.dest, call.time + timeOfWay]
                        return list
            # both of them are going down
            if call.ud & (self.dest - self.src) < 0:
                if self.src - abs(timeSource - call.time) * self.speed >= call.source:
                    # the call is inside the way of the elevator
                    if call.source <= self.src & call.dest >= self.dest:
                        curPosElev = self.src - self.speed * abs(call.time - timeSource)
                        timeOfWay = abs(call.dest - curPosElev) / self.speed + 2 * computeTime - self.startTime - self.closeTime
                        # list = [timeOfWay, call.source, self.dest, self.time + 2 * computeTime]
                        list = [timeOfWay, call.source, self.dest, call.time + timeOfWay]
                        return list
                    # the call src is inside and dest is outside
                    if self.src >= call.source & call.dest <= self.dest:
                        curPosElev = self.src - self.speed * abs(call.time - timeSource)
                        timeOfWay = abs(call.dest - curPosElev) / self.speed + 2 * computeTime - self.startTime - self.closeTime
                        # list = [timeOfWay, call.source, call.dest, self.time + 2 * computeTime + abs(call.dest - self.dest) / self.speed]
                        list = [timeOfWay, call.source, call.dest, call.time + timeOfWay]
                        return list
                    # the call src and dest is outside
                    if call.source < self.dest & call.dest < self.dest:
                        timeOfWay = self.time + abs(call.dest - self.dest) / self.speed + 2 * computeTime
                        # list = [timeOfWay, call.source, call.dest, self.time + timeOfWay]
                        list = [timeOfWay, call.source, call.dest, call.time + timeOfWay]
                        return list
        # they are in opposite direction
        timeOfWay = self.time - call.time + abs(self.dest - call.source) / self.speed + ds2 / self.speed + computeTime*2 - self.closeTime
        # list = [timeOfWay, call.source, call.dest, self.time + timeOfWay]
        list = [timeOfWay, call.source, call.dest, call.time + timeOfWay]
        return list

