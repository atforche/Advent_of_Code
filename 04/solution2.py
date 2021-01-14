import re

with open("input.txt", "r") as inFile:
    content = inFile.read().split("\n\n")
    input = [line.replace("\n", " ") for line in content]

valid = 0
    
for i in range(len(input)):
    validTerms = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    if all(x in input[i] for x in validTerms):
        
        fields = input[i].split()
        fieldsValid = True
        for field in fields:
            fieldValue = field[:3]

            if fieldValue == "byr":
                if re.fullmatch("byr:[0-9]{4}", field) == None:
                    fieldsValid = False
                else:
                    value = field[-4:]
                    if not(value.isdigit() and int(value) >= 1920 and int(value) <= 2002):
                        fieldsValid = False


            elif fieldValue == "iyr":
                if re.fullmatch("iyr:[0-9]{4}", field) == None:
                    fieldsValid = False
                else:
                    value = field[-4:]
                    if not(value.isdigit() and int(value) >= 2010 and int(value) <= 2020):
                        fieldsValid = False


            elif fieldValue == "eyr":
                if re.fullmatch("eyr:[0-9]{4}", field) == None:
                    fieldsValid = False
                else:
                    value = field[-4:]
                    if not(value.isdigit() and int(value) >= 2020 and int(value) <= 2030):
                        fieldsValid = False

            elif fieldValue == "hgt":
                unit = field[-2:]
                if unit == "cm":
                    value = field[-5:-2]
                    if not(value.isdigit() and int(value) >= 150 and int(value) <= 193 ):
                        fieldsValid = False
                elif unit == "in":
                    value = field[-4:-2]
                    if not(value.isdigit() and int(value) >= 59 and int(value) <= 76):
                        fieldsValid = False
                else:
                    fieldsValid = False

            elif fieldValue == "hcl":
                if re.fullmatch("#[0-9a-f]{6}", field[-7:]) == None:
                    fieldsValid = False

            elif fieldValue == "ecl":
                if field[-3:] not in ["amb","blu","brn","gry","grn","hzl","oth"]:
                    fieldsValid = False

            elif fieldValue == "pid":
                if re.fullmatch("pid:[0-9]{9}", field) == None:
                    fieldsValid = False

        if fieldsValid:
            valid += 1
            print(fields)

print(valid)