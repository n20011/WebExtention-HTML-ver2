a, op, b, _, c = input().split()



def X(a, b, c):
    if a == 'x':
        return 'a'
    
    if b == 'x':
        return 'b'
    
    return 'c'


if 'a' == X(a, b, c):
    if op == '+':
        print(int(c) - int(b))
    else:
        print(int(c) + int(b))

elif 'b' == X(a, b, c):
    if op == '+':
        print(int(c) - int(a))
    else:
        print(int(a) - int(c))

else:
    if op == '+':
        print(int(a) + int(b))
    else:
        print(int(a) - int(b))