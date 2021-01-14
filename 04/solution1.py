import re

with open("input.txt", "r") as inFile:
    content = inFile.read().split("\n\n")
    input = [line.replace("\n", " ") for line in content]
    
validTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0
for i in range(len(input)):
    if all(x in input[i] for x in validTerms):
        valid += 1

print(valid)