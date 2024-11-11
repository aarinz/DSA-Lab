def evaluate_postfix(expression):
    stack = []
    
    for char in expression.split():
        if char.isdigit():  
            stack.append(int(char))
        else:  
            operand2 = stack.pop()
            operand1 = stack.pop()
           
            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 / operand2
                
            stack.append(result)
    
    return stack.pop()

postfix_expr = "5 1 2 + 4 * + 3 -"
result = evaluate_postfix(postfix_expr)
print(f"Result of postfix expression '{postfix_expr}': {result}")
