from pandas import read_table
import re

def numTreeCollisions(slope):
    input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

    x = 0
    y = 0
    trees = 0

    while (y < len(input)):
        if (input[y][0][x] == "#"):
            trees += 1
        x = (x + slope[0]) % len(input[y][0])
        y = y + slope[1]
    return trees

output = numTreeCollisions((1,1)) * numTreeCollisions((3,1)) * \
     numTreeCollisions((5,1)) * numTreeCollisions((7,1)) * numTreeCollisions((1,2))
print(output)