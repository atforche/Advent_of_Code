from pandas import read_table

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

maxSeatID = float('-inf')
for i in range(len(input)):
    maxSeatID = max(maxSeatID, getSeatID(input[i][0]))
print(maxSeatID)