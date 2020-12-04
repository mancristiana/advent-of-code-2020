# https://adventofcode.com/2020/day/4

import re

fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
eyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def getPattern(field):
    return field + '([#\d\w]+)\s'

def validateField(passport, field):
    pattern = getPattern(field)
    captureGroups = re.search(pattern, passport)
    value = captureGroups.group(1)

    if field == "byr:":
        value = int(value)
        return 1920 <= value and value <= 2002
    elif field == "iyr:":
        value = int(value)
        return 2010 <= value and value <= 2020
    elif field == "eyr:":
        value = int(value)
        return 2010 <= value and value <= 2030
    elif field == "hgt:":
        if ("cm" in value):
            value = int(value.replace("cm", ""))
            return 150 <= value and value <= 193
        elif ("in" in value):
            value = int(value.replace("in", ""))
            return 59 <= value and value <= 76
        else:
            return False
    elif field == "hcl:":
        return re.match('^#([0-9a-f]{6})$', value)
    elif field == "ecl:":
        for color in eyeColors:
            if value == color:
                return True
    elif field == "pid:":
         return re.match('^([\d]{9})$', value)
    else:
        return False

def validatePassport(passport):
    for field in fields:
        if not field in passport:
            return False
        if not validateField(passport, field):
            pattern = getPattern(field)
            captureGroups = re.search(pattern, passport)
            value = captureGroups.group(1)
            return False

    return True

def getValidPassportCountFromPassports(passports):
    validPassportCount = 0
    for passport in passports:
        if validatePassport(passport):
            validPassportCount += 1

    return validPassportCount

def getPassportsFromData(data):
    tokens = data.split("\n\n")
    passports = []
    for passport in tokens:
        passport = passport.replace("\n", " ")
        passport = passport + " "
        passports.append(passport)

    return passports

with open('input.txt') as file:
    data = file.read()
    passports = getPassportsFromData(data)
    print(getValidPassportCountFromPassports(passports))