# https://adventofcode.com/2020/day/4

fields = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

def validatePassport(passport):
    isValid = True
    for field in fields:
        if not field in passport:
            isValid = False
            break

    return isValid

def getValidPassportCountFromPassports(passports):
    validPassportCount = 0
    for passport in passports:
        if validatePassport(passport):
            validPassportCount += 1

    return validPassportCount

def getPassportsFromData(data):
    passports = data.split("\n\n")
    for passport in passports:
        passport.replace("\n", " ")

    return passports

with open('input.txt') as file:
    data = file.read()
    passports = getPassportsFromData(data)
    print(getValidPassportCountFromPassports(passports))