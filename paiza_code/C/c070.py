N = int(input())



def poker(a, b, c, d):
    if a == b == c == d:
        return 'Four Card'
    
    if a == b == c or a == c == d or b == c == d:
        return 'Three Card'
    
    if a == b and c == d or a == c and b == d or a == d and b == c:
        return 'Two Pair'
    
    if a != b != c != d :
        return 'No Pair'
    
    return 'One Pair'



for _ in range(N):
    a, b, c, d = input()
    print(poker(a, b, c, d))