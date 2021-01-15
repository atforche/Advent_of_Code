from pandas import read_table
class Solution:

    def __init__(self):
        input = read_table("input.txt", delimiter="\n", header=None).to_numpy()

        split_input = [input[i][0].split(" bags contain ") for i in range(len(input))]

        self.key_colors = [item[0] for item in split_input]
        self.contains_colors = [[string.replace(".", "") for string in item[1].split(", ")] for item in split_input]
        self.color_counts = [[int(string[0:1]) if string[0:1].isdigit() else 0 for string in item] for item in self.contains_colors]
        self.contains_colors = [[string[2:len(string)-4].strip() for string in item] for item in self.contains_colors]

        self.colorMappings = {}
        for i in range(len(self.key_colors)):
            self.colorMappings[self.key_colors[i]] = [self.contains_colors[i], self.color_counts[i]]
    
    def recursiveSearch(self, color):
        total_count = 0
        if color in self.colorMappings:
            for i in range(len(self.colorMappings[color][0])):
                print(self.colorMappings[color][1][i])
                total_count += self.colorMappings[color][1][i] + (self.colorMappings[color][1][i] * self.recursiveSearch(self.colorMappings[color][0][i]))
        return total_count
        

    def outerBags(self, color):
        return self.recursiveSearch(color)

solver = Solution()
print(solver.outerBags("shiny gold"))