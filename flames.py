f=["f","l","a","m","e","s"]

FLAMES_MAP = {
    'f': 'Friends',
    'l': 'Love',
    'a': 'Affection',
    'm': 'Marriage',
    'e': 'Enemy',
    's': 'Sibling'
}

def flames(f, stack, index=0, name1=None, name2=None):
    if len(f) == 1:
        rel = FLAMES_MAP.get(f[0], f[0])
        return f"Relationship between {name1} and {name2} is: {rel}"
    l = len(stack) % len(f)
    if l == 0:
        l = len(f)
    index = (index + l - 1) % len(f)
    f.pop(index)
    return flames(f, stack, index, name1, name2)

def flames_calculator(name1, name2):
    stack = []
    stack2 = []
    for i in range(len(name1)):
        stack.append(name1[i])
    for i in name2:
        if i in stack:
            stack.remove(i)
        else:
            stack2.append(i)
    for i in stack2:
        stack.append(i)
    return stack

if __name__ == '__main__':
    while(True):
        name1 = str(input("enter the name 1 "))
        name2 = str(input("enter the name 2"))
        new_stack = flames_calculator(name1.lower(), name2.lower())
        print(new_stack)
        print(flames(["f","l","a","m","e","s"], new_stack, 0, name1, name2))
    
    
    
    
    
    
    
    
    
    