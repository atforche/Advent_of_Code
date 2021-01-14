with open("input.txt", "r") as inFile:
    content = inFile.read().split("\n\n")
    input = [line.replace("\n", "") for line in content]

total = 0
for i in range(len(input)):
    total += len(set(input[i]))

print(total)