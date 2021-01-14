with open("input.txt", "r") as inFile:
    content = inFile.read().split("\n\n")
    input = [line.replace("\n", " ") for line in content]

total = 0
for i in range(len(input)):
    people = input[i].split()
    total += sum([all([(character in person) for person in people]) for character in people[0]])
    

print(total)