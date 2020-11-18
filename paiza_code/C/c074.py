H, W, X = input().split()
h, w, x = int(H), int(W), int(X)

L = []
for _ in range(h):
    L += input()
word_L = ''.join(L)


#print(word_L)
#print(word_L.replace(word_L[:x], ''))


while len(word_L) >= x:
    print(word_L[:x])
    word_L = word_L.replace(word_L[:x], '')

print(word_L)