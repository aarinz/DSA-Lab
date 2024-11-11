output = []
operators = []
priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
expression = input("Enter the infix expression:")

def infix_to_postfix(expression):
    for i in expression:
        if i == '(':
            operators.append(i)
        elif i == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  
        elif i in priority:
            while (operators and operators[-1] != '(' and priority.get(i, 0) <= priority.get(operators[-1], 0)):
                output.append(operators.pop())
            operators.append(i)
        else:
            output.append(i)
            
    while operators:
        output.append(operators.pop())
    return "".join(output)

print(infix_to_postfix(expression))
