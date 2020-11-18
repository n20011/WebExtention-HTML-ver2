n = int(input())
box_u = []
box_k = []
for _ in range(n):
    user, word = input().split()
    box_u.append(word)
    box_k.append(user)



m = int(input())
DICT = {}
for _ in range(m):
    word_m, keyword = input().split()
    DICT[word_m] = keyword



for N in range(len(box_u)):
    print(f'{box_k[N]} {DICT[box_u[N]]}')