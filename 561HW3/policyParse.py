import numpy as np

def printDirection():
    DemoDirection = ['←','↑','→','↓']
    for y in range(sizeOfGrid):
        line = ""
        for x in range(sizeOfGrid):
            if mapGrid[y,x] >= 0:
                line += DemoDirection[mapGrid[y,x]] + ' '
            else:
                line += '. '
        print(line)

inputFile = open('policy1.txt')
sizeOfGrid = 10
numOfCar = 5
mapGrid = np.mat(-np.ones((sizeOfGrid, sizeOfGrid), np.int8))
for car in range(numOfCar):
    for i in range(sizeOfGrid * sizeOfGrid):
        temp = inputFile.readline().split(": ")
        temp = temp
        pos = tuple(int(''.join(c for c in x if c.isdigit())) for x in temp[0].split(','))
        if 'None\n' not in temp[1]:
            direction = tuple(int(''.join(c for c in x if c.isdigit() or c =='-')) for x in temp[1].split(','))
            if direction[1] == -1:
                mapGrid[pos] = 0
            elif direction[0] == -1:
                mapGrid[pos] = 1
            elif direction[1] == 1:
                mapGrid[pos] = 2
            elif direction[0] == 1:
                mapGrid[pos] = 3
        else:
            mapGrid[pos] = -1
    printDirection()
    print("-----------------------------")
