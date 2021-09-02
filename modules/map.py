import json
from random import randint


Tablero = list(map(lambda x: [" "]*6, range(6)))
r = randint(0,1)
Tablero[2+r][2] = "x"
Tablero[3-r][2] = "o"
Tablero[3-r][3] = "x"
Tablero[2+r][3] = "o"
actual_position = (2+r, 2)

mapsJson = json.load(open("data/maps.json"))

def getMap():
    global actual_position
    if(actual_position[1] == 5 and actual_position[0] == 0):
        return mapsJson['down-left']
    elif(0 < actual_position[1] < 5 and actual_position[0] == 0):
        return mapsJson['center-left']
    elif(actual_position[1] == 0 and actual_position[0] == 0):
        return mapsJson['up-left']
    elif(0 < actual_position[0] < 5 and actual_position[1] == 0):
        return mapsJson['up-center']
    elif(actual_position[0] == 5 and actual_position[1] == 0):
        return mapsJson['up-right']
    elif(0 < actual_position[1] < 5 and actual_position[0] == 5):
        return mapsJson['center-right']
    elif(actual_position[0] == 5 and actual_position[1] == 5):
        return mapsJson['down-right']
    elif(0 < actual_position[0] < 5 and actual_position[1] == 5):
        return mapsJson['down-center']
    else:
        return mapsJson['center-center']

def setPosition(portal_used):
    global actual_position
    if(portal_used == "left"):
        if(actual_position[0] > 0):
            actual_position = (actual_position[0]-1, actual_position[1])
    elif(portal_used == "up"):
        if(actual_position[1] > 0):
            actual_position = (actual_position[0], actual_position[1]-1)
    elif(portal_used == "right"):
        if(actual_position[0] < 5):
            actual_position = (actual_position[0]+1, actual_position[1])
    elif(portal_used == "down"):
        if(actual_position[1] < 5):
            actual_position = (actual_position[0], actual_position[1]+1)

def inSelect():
    if(Tablero[actual_position[0]][actual_position[1]] == "x"):
        return True
    else:
        return False
def inLost():
    if(Tablero[actual_position[0]][actual_position[1]] == "o"):
        return True
    else:
        return False

def printTablero():
    print("".join(["-"]*(2**6)))
    for row in Tablero:
        print(row)
    print("".join(["-"]*(2**6)))