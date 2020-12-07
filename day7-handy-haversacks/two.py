
def getCountOfInnerBags(ruleMap, outerBag):
    innerBags = ruleMap[outerBag]
    if (innerBags[0] == "no other"):
        return 0
    else:
        count = 0
        for innerBag in innerBags:
            innerBagCount = int(innerBag[:1])
            count += innerBagCount + innerBagCount * getCountOfInnerBags(ruleMap, innerBag[2:])
        return count

def getRuleMap(rules):
    ruleMap = {}

    for rule in rules:
        tokens = rule.split(" bags contain ")
        outerBag = tokens[0]
        innerBags = tokens[1].replace(" bags", "").replace(" bag", "").replace(".", "").split(", ")
        ruleMap[outerBag] = innerBags

    return ruleMap

def getBagCountInsideShinyGold(rules):
    ruleMap = getRuleMap(rules)
    count = getCountOfInnerBags(ruleMap, "shiny gold")
    return count

with open('input.txt') as file:
    data = file.read()
    rules = data.split("\n")
    print(getBagCountInsideShinyGold(rules))
