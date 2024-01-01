


def infix_to_postfix(expression):
    
    stack = []
    output = ""
    precedence = {'+':1,'-':1, '*':2, '/':2, '^':3}
    
    
    def is_operator(c):
        return c in precedence    
    
    def is_operand(c):
        return c.isalnum()
    
    def greater_than(a, b):
        try:
            return precedence[a] >= precedence[b]
        except KeyError:
            return False
        except:
            return False
       
    for c in expression:
        if is_operand(c):
            output += c
        elif c =="(":
            stack.append(c)
        elif c==')':
            while stack and stack[-1] != '(' :
                output += stack.pop()
            stack.pop()
        else:
            while stack and is_operator(stack[-1]) and greater_than(c, stack[-1]):
                output += stack.pop()
            stack.append(c)
    
    while stack:
        output += stack.pop()

    return output


print(infix_to_postfix('(a*b)+(c*d)'))

print(infix_to_postfix('a+b*(c^d-e)^(f+g*h)-i'))