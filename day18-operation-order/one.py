
def main():
    with open('input.txt') as file:
        expressions = file.read().split("\n")
    print(solve(expressions))

def solve(expressions):
    sum = 0
    for expression in expressions:
        result, index = evaluate(expression.replace(" ", ""), 0)
        print(result)
        sum += result
    
    return sum

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

main()
