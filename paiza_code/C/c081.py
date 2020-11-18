panunber = int(input())
n_L = 0
n_R = 0
count = 0

socks_L = list()
socks_R = list()

for _ in range(nunber):
    word, RL = input().split()

    if RL == 'L':
        socks_L += word, RL
    else:
        socks_R += word, RL

print(socks_R, socks_L)




while len(socks_L) != 0 or len(socks_R) != 0:
    if socks_L[0] == socks_R[n_R]:
        count += 1
        socks_L.remove
        socks_R.remove
        if len(socks_L) != 0 or len(socks_R) != 0:
            socks_L.remove
            socks_R.remove
        
    else:
        n_R += 2
        
print(socks_R, socks_L)
print(count)
print(len(socks_L))