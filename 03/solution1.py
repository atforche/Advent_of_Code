from pandas import read_table
import re

valid = 0
input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

x = 0
y = 0
trees = 0

slope = (3,1)
while (y < len(input)):
    if (input[y][0][x] == "#"):
        trees += 1
    x = (x + slope[0]) % len(input[y][0])
    y = y + slope[1]

print(trees)