
def containsShinyGold(ruleMap, outerBag):

    innerBags = ruleMap[outerBag]
    if (innerBags[0] == "no other"):
        return False
    else:
        for innerBag in innerBags:
            if ("shiny gold" in innerBag):
                return True
            elif (containsShinyGold(ruleMap, innerBag[2:])):
                return True
        return False

def getRuleMap(rules):
    ruleMap = {}

    for rule in rules:
        tokens = rule.split(" bags contain ")
        outerBag = tokens[0]
        innerBags = tokens[1].replace(" bags", "").replace(" bag", "").replace(".", "").split(", ")
        ruleMap[outerBag] = innerBags

    return ruleMap

def getBagCountContainingShinGold(rules):
    ruleMap = getRuleMap(rules)
    count = 0
    for bag in ruleMap:
        if (containsShinyGold(ruleMap, bag)):
            count += 1
            print(bag)
    return count

with open('input.txt') as file:
    data = file.read()
    rules = data.split("\n")
    print(getBagCountContainingShinGold(rules))
