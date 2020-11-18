Q = int(input())

def divisor(n): 
    i = 1
    table = []
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table



def Jatch(N, P):
    if N == P:
        return 'perfect'
    if N == P + 1:
        return 'nearly'
    return 'neither'



for _ in range(Q):
    N = int(input())
    P = sum(divisor(N)) - N
    print(Jatch(N, P))