stack =  []
precedence =  {"+":2, "-":2, "*":3, "/":3, "^":4}

def is_operand(c):
    return c.isalnum()

def check_precedence(c1):
    try:
        return  precedence[c1] <= precedence[stack[-1]]
    except KeyError:
        return False
    except:
        return False
    
def is_operator(character):
    return character in precedence

def infix_to_prefix(expresssion):
    expresssion =  ''.join([ ')' if c =='(' else '(' if c==')' else c for c in expresssion])
    expresssion = expresssion[::-1]
    prefix = ''
    for c in expresssion:
        if(is_operand(c)):
            prefix +=c
        elif c == '(':
            stack.append(c)
        elif c ==')':
            while stack and stack[-1]!='(':
                prefix += stack.pop()
            stack.pop()
        else:
            while stack  and check_precedence(c) and is_operator(stack[-1]):
                prefix += stack.pop()
            stack.append(c)
            
    
    while len(stack)>0:
        prefix += stack.pop()
    
    print(prefix)
    return prefix[::-1]

print(infix_to_prefix("a+b*(c^d-e)^(f+g*h)-i"))