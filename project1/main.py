import csv
import sys
# import json
from Call import Call
from elevator import elevator
from Building import Building

if __name__ == '__main__':
    files = sys.argv
    buildingFile = files[1]
    callsFile = files[2]
    outFile = sys.argv[3]

    # reading from the csv calls
    callList = []
    with open('Calls_a.csv', mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            ud = int( row[3])-int(row[2])
            if ud > 0:
                ud=1
            else:
                ud=-1
            call = Call(row[0], float(row[1]), int(row[2]), int(row[3]), ud , int(row[4]), int(row[5]))
            callList.append(call)

    # reading from the json buildings
    Building = Building('B1.json')
    with open('out.csv', 'w', newline="") as file:
        csvwrite = csv.writer(file)
        elevList = []
        # make list of elevator
        for i in Building.elevators:
            elevs = elevator(_id=i["_id"], speed=i["_speed"], minFloor=i["_minFloor"],
                            maxFloor=i["_maxFloor"], closeTime=i["_closeTime"], openTime=i["_openTime"],
                            startTime=i["_startTime"], stopTime=i["_stopTime"], src=0,
                            dest=0, time=0) # src\dest = the src\dest of the last call the elevator except.  time is the when the elevator end work
            elevList.append(elevs)
        # for every call check all the elevators
        countcall = 0
        for j in callList:
            maxValue = sys.maxsize
            indexElev = 0
            countElev = 0
            for i in elevList:
                elev = i
                list1 = []
                list1 = elev.__calc__(j)
                time = list1[0]
                source0 = list1[1]
                dest0 = list1[2]
                time0 = list1[3]
                if time < maxValue:
                    maxValue = time
                    indexElev = countElev
                    source1 = source0
                    dest1 = dest0
                    time1 = time0
                countElev = countElev + 1
            elevList[indexElev].setSrc(source1)
            elevList[indexElev].setDest(dest1)
            elevList[indexElev].setTime(time1)
            j.setElevator(indexElev)
            countcall = countcall + 1
            csvwrite.writerow(j.__str__())

















