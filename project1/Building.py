import json
from elevator import elevator


class Building:

    # Let's upload the JSON file
    def __init__(self, file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
                self.minFloor = data["_minFloor"]
                self.maxFloor = data["_maxFloor"]
                self.numF = (self.maxFloor - self.minFloor)
                elevators = []
                for el in data["_elevators"]:
                    # elev = elevators[el]
                    elevators.append(el)
                self.elevators = elevators.copy()
                self.numE = len(self.elevators)
        except IOError as e:
            print(e)





    # def __calc__(self, call) -> int:
    #      ds1 = abs(self.dest - call.source)
    #      ds2 = abs(call.dest - call.source)
    #      timeOfWay = 2 * self.startTime + ds1 / self.speed + 2 * self.stopTime + 2 * self.openTime + self.closeTime + ds2 / self.speed
    #      if self.timeEnd <= call.time:
    #         return timeOfWay, call.src, call.dest
    #      if self.timeEnd > call.time:
    #              # both of them are going up
    #              if call.ud & (self.dest - self.src) > 0 & call.source <= self.src:
    #                  if self.time + abs(self.src - call.source) / self.speed + 2 * self.startTime + 2 * self.stopTime + 2 * self.openTime + self.closeTime + ds2 / self.speed < call.time:
    #                     # the call is inside the way of the elevator
    #                     if self.src <= call.source & call.dest <= self.dest:
    #                         timeOfWay = abs(self.src - self.dest) / self.speed + 4 * self.stopTime + 4 * self.closeTime + 4 * self.openTime + 4 * self.startTime
    #                         return timeOfWay, call.source, self.dest
    #                     # the call src is inside and the dest is outside
    #                     if self.src <= call.source & call.dest >= self.dest:
    #                         timeOfWay = abs(self.src - self.dest) / self.speed + 4 * self.stopTime + 4 * self.closeTime + 4 * self.openTime + 4 * self.startTime
    #                         return timeOfWay, call.source, self.dest
    #                     # the call src and dest is outside
    #                     if call.src > self.dest & call.dest > self.dest:
    #
    #              # both of them are going down
    #              if call.ud & (self.dest - self.src) > 0 & call.source <= self.src:
    #                  # the call is inside the way of the elevator
    #                  if self.src <= call.source & call.dest <= self.dest:
    #                     timeOfWay = abs(self.src - self.dest) / self.speed + 4 * self.stopTime + 4 * self.closeTime + 4 * self.openTime + 4 * self.startTime
    #                     return timeOfWay, call.source, self.dest
    #                  # the call src and dest is outside
    #                  if self.src <= call.source & call.dest >= self.dest:
    #                      timeOfWay = abs(self.src - self.dest) / self.speed + 4 * self.stopTime + 4 * self.closeTime + 4 * self.openTime + 4 * self.startTime
    #                      return timeOfWay, call.source, self.dest
    #                  # the call src and dest is outside
    #                  if call.src > self.dest & call.dest > self.dest:
    #         # they are in opposite direction
    #         else:
    #             return timeOfWay, call.src, call.dest

