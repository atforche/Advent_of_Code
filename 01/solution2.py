from pandas import read_table

input = read_table("input.txt", delimiter="\n").to_numpy()

for i in range(len(input)-2):
    for j in range(i+1, len(input)-1, 1):
        for k in range(j+1, len(input), 1):
            if input[i] + input[j] + input[k] == 2020:
                print(input[i] * input[j] * input[k])