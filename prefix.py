def infix_to_prefix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def less_or_equal_precedence(i, o):
        return precedence.get(i, 0) <= precedence.get(o, 0)
    def is_operator(c):
        return c in precedence
    def not_greater(i, o):
        try:
            a = precedence[i]
            b = precedence[o]
            return True if a <= b else False
        except KeyError:
            return False
    def is_operand(ch):
        return ch.isalnum()
    stack = []
    prefix = ''
    # Reverse infix expression
    infix_expression = infix_expression[::-1]
    # Replace '(' with ')' and vice versa
    infix_expression = ''.join(['(' if c == ')' else ')' if c == '(' else c
                                for c in infix_expression])
    print(infix_expression)
    
    for c in infix_expression:
        print('character ',c)
        if is_operand(c):
            prefix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                prefix += stack.pop()
            stack.pop()
        else:
            while (stack and not_greater(c, stack[-1])):
                prefix += stack.pop()
            stack.append(c)
            
    while stack:
        prefix += stack.pop()
    # Reverse prefix expression
  
    prefix = prefix[::-1]
    return prefix

# Test case
infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
prefix_expression = infix_to_prefix(infix_expression)
print("Infix:", infix_expression)
print("Prefix:", prefix_expression)


# infix_expression = "a+(g^b-i/h*c^d)-f"
# prefix_expression = infix_to_prefix(infix_expression)
# print("Infix:", infix_expression)
# print("Prefix:", prefix_expression)

# infix_expression = "(a*b)+(c*d)"
# prefix_expression = infix_to_prefix(infix_expression)
# print("Infix:", infix_expression)
# print("Prefix:", prefix_expression)

def infix_to_postfix(infix_expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    def is_operand(ch):
        return ch.isalnum()
    def is_operator(c):
        return c in precedence
    def not_less(i, o):
        try:
            a = precedence[i]
            b = precedence[o]
            return a >= b
        except KeyError:
            return False

    stack = []
    postfix = ''
    for c in infix_expression:
        if is_operand(c):
            postfix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and is_operator(stack[-1]) and not_less(c, stack[-1]):
                postfix += stack.pop()
            stack.append(c)
    while stack:
        postfix += stack.pop()
    return postfix

infix_expression = "(a*b)+(c*d)"
prefix_expression = infix_to_postfix(infix_expression)
print("Infix:", infix_expression)
print("Postfix:", prefix_expression)

infix_expression = "a+b*(c^d-e)^(f+g*h)-i"
prefix_expression = infix_to_postfix(infix_expression)
print("Infix:", infix_expression)
print("Postfix:", prefix_expression)