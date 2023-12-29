operators = ['+','-','*','/','^']

def prefixExpression(userString):
    
    user_input = list(userString)
    stack = []
    expression = []

    for char in user_input:
        if char in operators:
            expression.append(char)
        else:
            stack.append(char)

    return ('').join(expression) + ('').join(stack)


# print(prefixExpression(input('Enter the expression we want the prefix expression for\n')))

# # (a+b)*(c+d)


# # (+ab)*(+cd)
# # *(+ab)(+cd)


def reverseString(str):
    stack = []
    for char in str:
        if char == ')':
            stack.append('(')
        elif char == '(':
            stack.append(')')
        else: 
            stack.append(char)

    return ''.join(stack[::-1])

def infixToPrefix(str = reverseString(input(f'\nEnter the infix string\n'))):
    
    stack = []
    operands = ['+','-','/','*','^']
    prefixString = ''
    for char in str:
        if char not in operands:
            stack.append(char)
            print(stack)
        if char in operands:
            prefixString += char
            print(prefixString)
        
    print(prefixString + ''.join(stack[::-1]))

# infixToPrefix()


dict = {}
i = 0 
while i<5:
    dict[input("Enter the keys")] = i
    i +=1
print(dict)