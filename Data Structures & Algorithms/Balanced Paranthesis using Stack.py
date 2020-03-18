from Stacks import *

def is_match(p1,p2):
    if p1=='(' and p2==')':
        return True
    elif p1 == '[' and p2 == ']':
        return True
    elif p1 == '{' and p2 == '}':
        return True
    else:
        return False



def balanced(string):
    s = Stack()
    is_balanced = True
    index = 0
    while index<len(string) and is_balanced:
        paren = string[index]
        if paren in '([{':
            s.push(paren)
        else:
            if s.isEmpty():
                is_balanced=False
            else:
                top = s.pop()
                if not is_match(top,paren):
                    is_balanced=False
        index+=1
    if s.isEmpty() and is_balanced:
        return True
    else:
        return False

print(balanced('{}'))
print(balanced('{]'))
