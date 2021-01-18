import numpy as np

with open("input.txt", "r") as inFile:
    content = inFile.read().split("\n\n")
    input = [[char for char in item] for item in content[0].split("\n")]

field = np.expand_dims(np.expand_dims(np.array(input[:]), 0),0)

def advanceConway(field):
    ## First pad the original field with layers so the checkNeighbors function
    ## doesn't have to worry about out of bounds indexing
    paddedField = np.pad(field, pad_width=1, mode="constant", constant_values=".")

    ## Now initialize a new field to write the new field into
    newField = np.full((len(paddedField), len(paddedField[0]), len(paddedField[0][0]), len(paddedField[0][0][0])),".")
    
    ## Now loop through and perform the update on every cell
    for i in range(len(newField)):
        for j in range(len(newField[0])):
            for k in range(len(newField[0][0])):
                for w in range(len(newField[0][0][0])):
                    activeNeighors = checkNeighbors(paddedField, i, j, k, w)
                    if paddedField[i][j][k][w] == ".":
                        if activeNeighors == 3:
                            newField[i][j][k][w] = "#"
                        else:
                            newField[i][j][k][w] = "."
                    else:
                        if activeNeighors == 2 or activeNeighors == 3:
                            newField[i][j][k][w] = "#"
                        else:
                            newField[i][j][k][w] = "."

    return newField

def checkNeighbors(field, x, y, z, w):
    total = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            for k in range(-1, 2, 1):
                for v in range(-1, 2, 1):
                    if x + i >= 0 and x + i < len(field):
                        if y + j >= 0 and y + j < len(field[0]):
                            if z + k >= 0 and z + k < len(field[0][0]):
                                if w + v >= 0 and w + v < len(field[0][0][0]):
                                    if i != 0 or j != 0 or k != 0 or v != 0:
                                        if field[x+i][y+j][z+k][w+v] == "#":
                                            total += 1
    return total



for i in range(6):
    field = advanceConway(field)

print(field.shape)
activeCells = np.sum(np.sum(np.sum(np.sum((field == "#"),axis=0),axis=0),axis=0))
print(activeCells)