#M=立候補の人数  N=有権者の人数  K=演説の回数
m, n, k = input().split()
M, N, K = int(m), int(n), int(k)

box = {}
for nn in range(M):
    box[nn + 1] = 0


def IS(box, nunber, M):
    List = []
    count = 0
    for nnn in range(M):
        if box[nnn + 1] > 0:
            box[nnn] -= 1
            count += 1
            box.uppend(nnn + 1)
    return [count, List]




for _ in range(K):
    nunber = int(input())
    if IS(box, nunber, M) == 0:
        if N > 0:
            box[nunber] += 1
        else:
            box[nunber] += 0
    
    elif IS(box, nunber, M) > 0:
        

print(box)
print(IS(box, nunber, M))