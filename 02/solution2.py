from pandas import read_table
import re

valid = 0
input = read_table("input.txt", delimiter="\n", header=None).to_numpy()
for i in range(len(input)):
    splitInput = input[i][0].split()
    indexes = splitInput[0].split("-")
    charOfInterest = splitInput[1][0]
    password = splitInput[2]

    bool1 = password[int(indexes[0])-1] == charOfInterest
    bool2 = password[int(indexes[1])-1] == charOfInterest
    if (bool1 or bool2) and not(bool1 == bool2):
        valid += 1

print(valid)