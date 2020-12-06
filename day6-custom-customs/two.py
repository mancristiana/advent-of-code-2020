
def getCountOfAnswersWhereEveryoneSaidYes(group):
    answers = group.split("\n")
    answersMap = {}
    for answer in answers:
        for letter in answer:
            if (letter in answersMap.keys()):
                answersMap[letter] += 1
            else:
                answersMap[letter] = 1 

    peopleCount = len(answers)
    count = 0
    for key in answersMap:
        if (answersMap[key] == peopleCount):
            count += 1
    
    return count

with open('input.txt') as file:
    data = file.read()
    groups = data.split("\n\n")

    count = 0
    for group in groups:
        count += getCountOfAnswersWhereEveryoneSaidYes(group)

    print(count)