from pandas import read_table

def processNums(numstr):
    if numstr[0] == "+":
        return int(numstr[1:])
    else:
        return -1 * int(numstr[1:])

input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

split_input = []
for i in range(len(input)):
    split_input.append(input[i][0].split())
    split_input[i][1] = processNums(split_input[i][1])


accumulator = 0
pc = 0

executedInstructions = set()

while True:
    if pc in executedInstructions:
        break
    else:
        executedInstructions.add(pc)
    if split_input[pc][0] == "acc":
        accumulator += split_input[pc][1]
        pc += 1
    elif split_input[pc][0] == "jmp":
        pc += split_input[pc][1]
    elif split_input[pc][0] == "nop":
        pc += 1

print(accumulator)