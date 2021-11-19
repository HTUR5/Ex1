# Ex1
## offline elevator algorithem <br>
### Hodaya Turgeman, Sivan Cohen <br>

In this assignment we are required for some amount of elevator calls, to embed the appropriate elevator in the building so that the average waiting time is minimal.\
For each call we are given the time it was received, the source floor and the destinision floor.\
<br>
We used the following links for gather information about this problem: <br>
https://www.youtube.com/watch?v=siqiJAJWUVg <br>
https://www.geeksforgeeks.org/smart-elevator-pro-geek-cup/
<br>
<br>
### The Offline Algorithem <br>
1. in the main class we are reading the calls.csv file and the building.json. <br>
while reading this files, we are creatig an object of each call and each elevator. <br>
so that in the end of the reading we have list of calls and list of elevators. <br>
2. we are passing the call list. for each call we are using the calc function for checking how much time this call take for every elevator in the elevator list. <br>
3. we are embes the call for the elevator which return the minimum time.

the calc function: <br>
for each elevator we have all the data about her id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime, src, dest, time. <br>
when src and dest are belong to the last call which the elevator worked on, and time refer to the ending time which the elevator end her work. <br>
we are calculate the time of each call for some elevator through the elevator class so we have access to this data. <br>
for each call we calculate the waiting time for the call, and the timeEnd for this elevator with the call, according to this option: <br>
1. the elevator endWork end befor the call time. <br>
2. if not: <br>
2.1: the call and the elevator is in the same direction and the elevator is not paassing the call source while it drive <br>
_1. the call src and dest is inside the elevator last call <br>
_2. the call src and dest is not inside the elevator last call <br>
_3. the call src is inside and the call dest is outside the elevator last call <br>
2.2  the call and the elevator is in opposite directions <br>

## time running

|  | call_a  | call_b | call_c | call_d |
| :---         |     :---:      |          ---: |     :---:      |          ---: | 
| B1   | 112/0     |      |          |         |
| B2     | 49/0      |       |           |           |
| B3    | 29/0     | 526/174     |    575/99      |          538/88  |
| B4           | 17/0           | 190/6        | 180/3       |     174/3    |  
| B5           | 11/0           | 34/0         | 33/0        |     34/0     |

## UML
https://lucid.app/lucidchart/a3b4b404-6420-460b-9ae9-4de73fa27d8f/edit?viewport_loc=-43%2C225%2C2858%2C1094%2C0_0&invitationId=inv_ad201736-4648-473f-8bbf-73c007e0df94

[diagram.pdf](https://github.com/HTUR5/Ex1/files/7567075/diagram.pdf)



