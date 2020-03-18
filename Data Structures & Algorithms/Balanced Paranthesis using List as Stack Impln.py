def paran(str):
    lst = []
    index=0
    is_balanced = True
    while index<len(str) and is_balanced:
        p = str[index]
        if p in '([{':
            lst.append(p)
        else:
            if lst==[]:
                is_balanced = False
            else:
                top = lst.pop()
                if not is_matching(top,p):
                    return False
        index+=1
    if lst==[] and is_balanced:
        return True
    else:
        return False

def is_matching(p1,p2):
     if p1=='(' and p2==')':
         return True
     elif p1=='[' and p2==']':
         return True
     elif p1=='{' and p2=='}':
         return True
     else:
         return False

print(paran('[()]'))
