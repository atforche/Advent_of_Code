from pandas import read_table
import re

valid = 0
input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

for i in range(len(input)):
    splitInput = input[i][0].split()
    minMax = splitInput[0].split("-")
    charOfInterest = splitInput[1][0]
    password = splitInput[2]

    if password.count(charOfInterest) >= int(minMax[0]) and password.count(charOfInterest) <= int(minMax[1]):
        valid = valid + 1

print(valid)