Vertical, Side = map(int, input().split())

a_1, a_2 = map(int, input().split())
b_1, b_2 = map(int, input().split())

box_V = []
V = 0
for _ in range(Vertical):
    box_V.append(a_1 + V)
    V += b_1 - a_1
print(box_V)




for n in range(Vertical):
    nunber = box_V[n]
    box_S = []
    S = a_2 - a_1
    for _ in range(Side):
        box_S.append(nunber)
        nunber += S
    print(' '.join(map(str, box_S)))