
def main():
    with open('input.txt') as file:
        expressions = file.read().split("\n")
    print(solve(expressions))

def solve(expressions):
    sum = 0
    for expression in expressions:
        expressionWithPrecedenceBrackets = addPrecedenceBrackets(expression.replace(" ", ""))
        result, index = evaluate(expressionWithPrecedenceBrackets, 0)
        print(expressionWithPrecedenceBrackets, result)
        sum += result
    
    return sum

def addPrecedenceBrackets(expression):
    newExpression = expression
    for n in range(expression.count("+")):
        newExpression = addPrecedenceBracketsForNthOperator(newExpression, n)
    return newExpression

def addPrecedenceBracketsForNthOperator(expression, n):
    nthIndex = expression.replace("+", " ", n).find("+")
    newExpression = expression[:]
    openBracketCount = 0
    for i in range(nthIndex - 1, -1, -1):
        token = newExpression[i]
        if (token == ")"):
            openBracketCount +=1
        elif (token == "("):
            openBracketCount -=1
            if (openBracketCount == 0):
                newExpression = newExpression[:i] + "(" + newExpression[i:]
                break   
        elif (openBracketCount == 0 and token.isdigit()):
            newExpression = newExpression[:i] + "(" + newExpression[i:]
            break

    for i in range(nthIndex + 2, len(newExpression)):
        token = newExpression[i]
        if (token == "("):
            openBracketCount +=1
        elif (token == ")"):
            openBracketCount -=1
            if (openBracketCount == 0):
                newExpression = newExpression[:i+1] + ")" + newExpression[i+1:]
                break
        elif (openBracketCount == 0 and token.isdigit()):
            newExpression = newExpression[:i+1] + ")" + newExpression[i+1:]
            break
    
    return newExpression

def evaluate(expression, startIndex):
    total = 0
    operation = add
    index = startIndex
    while index < len(expression):
        token = expression[index]
        if (token == "+"):
            operation = add
            index += 1
        elif (token == "*"):
            operation = multiply
            index += 1
        elif (token == "("):
            resultTotal, resultIndex = evaluate(expression, index + 1)
            total = operation(total, resultTotal)
            index = resultIndex
        elif (token == ")"):
            return total, index + 1
        else:
            total = operation(total, int(token))
            index += 1
    return total, index

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    main()
