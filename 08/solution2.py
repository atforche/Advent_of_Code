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


def executeProgram(instructions):
    accumulator = 0
    pc = 0
    executedInstructions = set()
    terminated = False
    while True:
        if pc in executedInstructions:
            break
        elif pc == len(instructions):
            terminated = True
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
    return accumulator, terminated

for i in range(len(split_input)):
    if split_input[i][0] == "nop":
        split_input[i][0] = "jmp"
        accumulator, terminated = executeProgram(split_input)
        if terminated:
            print(accumulator)
            break
        else:
            split_input[i][0] = "nop"
    elif split_input[i][0] == "jmp":
        split_input[i][0] = "nop"
        accumulator, terminated = executeProgram(split_input)
        if terminated:
            print(accumulator)
            break
        else:
            split_input[i][0] = "jmp"