
def getCountOfAnswersWhereAnyoneSaidYes(group):
    answers = group.split("\n")
    uniqueAnswers = []
    for answer in answers:
        for letter in answer:
            if (letter not in uniqueAnswers):
                uniqueAnswers.append(letter)

    # print(uniqueAnswers, len(uniqueAnswers))

    return len(uniqueAnswers)

with open('input.txt') as file:
    data = file.read()
    groups = data.split("\n\n")

    count = 0
    for group in groups:
        count += getCountOfAnswersWhereAnyoneSaidYes(group)

    print(count)