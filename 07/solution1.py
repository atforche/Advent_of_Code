from pandas import read_table
class Solution:

    def __init__(self):
        input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

        split_input = [input[i][0].split(" bags contain ") for i in range(len(input))]

        self.key_colors = [item[0] for item in split_input]
        self.contains_colors = [[string.replace(".", "") for string in item[1].split(", ")] for item in split_input]
        self.contains_colors = [[string[2:len(string)-4].strip() for string in item] for item in self.contains_colors]

        self.colorMappings = {}
        for i in range(len(self.key_colors)):
            for j in range(len(self.contains_colors[i])):
                if self.contains_colors[i][j] in self.colorMappings:
                    self.colorMappings[self.contains_colors[i][j]].append(self.key_colors[i])
                else:
                    self.colorMappings[self.contains_colors[i][j]] = [self.key_colors[i]]

        self.exploredSet = set()

    
    def recursiveSearch(self, color):
        if color not in self.colorMappings or len(self.colorMappings[color]) == 0:
            return
        else:
            for searchColor in self.colorMappings[color]:
                if searchColor not in self.exploredSet:
                    self.exploredSet.add(searchColor)
                    self.recursiveSearch(searchColor)

    def outerBags(self, color):
        self.recursiveSearch(color)
        return len(self.exploredSet)

solver = Solution()
print(solver.outerBags("shiny gold"))