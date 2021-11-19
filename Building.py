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
                elevators = []
                for el in data["_elevators"]:
                    # elev = elevators[el]
                    elevators.append(el)
                self.elevators = elevators.copy()
        except IOError as e:
            print(e)


