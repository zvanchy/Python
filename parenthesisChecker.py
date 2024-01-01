def checkParenthesis(userInput):
    stack = []
    openingSymbols = ['(', '{', '[']
    closing_symbols = [')', '}', ']']
    brackets_dictionary = {')':'(', '}':'{', ']':'['}
    
      
    for char in userInput:
        if char in openingSymbols:
            stack.append(char)
        elif char in closing_symbols:
            if len(stack)!=0 and stack.pop() == brackets_dictionary[char]:
                continue
            else:
                return False
        else:
            continue
        
    # if the stack is not empty that means there 
    # is imbalance in the stack
    
    if(len(stack)>0):
        return False
    else:
        return True


result = checkParenthesis(input('Enter the string to check for parentesis '))
if(result):
    print("Input has correct parenthesis")
else:
    print('Input has errors in parenthesis')