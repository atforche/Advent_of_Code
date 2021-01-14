from pandas import read_table
import numpy as np

input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

def getRow(inputString):
    rows = inputString[0:7]
    lower = 0
    upper = 127
    for i in range(len(rows)):
        mid = (upper + lower) // 2
        if rows[i] == "F":
            upper = mid
        else:
            lower = mid + 1

    return lower

def getSeat(inputString):
    seats = inputString[7:]
    lower = 0
    upper = 7
    for i in range(len(seats)):
        mid = (upper + lower) // 2
        if seats[i] == "L":
            upper = mid
        else:
            lower = mid + 1

    return lower

def getSeatID(inputString):
    return 8 * getRow(inputString) + getSeat(inputString)

seatIds = np.zeros(input.shape)
for i in range(len(input)):
    seatIds[i] = getSeatID(input[i][0])
seatIds = np.sort(seatIds, axis=0)
for i in range(len(seatIds)-1):
    if seatIds[i+1][0]-seatIds[i][0] == 2:
        print(seatIds[i]+1)

# print(seatIds)