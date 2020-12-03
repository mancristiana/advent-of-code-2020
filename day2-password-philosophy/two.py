# https://adventofcode.com/2020/day/2

import re

pattern = '^(\d+)-(\d+) ([a-z]): ([a-z]+)$'

def validatePassword(line):
    captureGroups = re.search(pattern, line)
    
    firstIndex = int(captureGroups.group(1)) - 1
    secondIndex = int(captureGroups.group(2)) - 1
    letter = captureGroups.group(3)
    password = captureGroups.group(4)

    return (password[firstIndex] == letter) != (password[secondIndex] == letter)

def getValidPasswordNumber(lines):
    validPasswords = 0
    for line in lines:
        isValid = validatePassword(line)
        if isValid:
            validPasswords += 1
    
    return validPasswords

with open('input.txt') as file:
    data = file.read()
    lines = data.split("\n")
    lines.pop()
    print(getValidPasswordNumber(lines))
