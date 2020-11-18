# [8:59 - (c + b )]  <--時間と照らし合わせる
# [8:59 - (c + b )] - a = A_.
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

MoveA = a
MoveB_C = b + c

move = 539 - MoveB_C
time = move // 60
minutes = move - time * 60


n = int(input())
train = []
test = []
for _ in range(n):
    test = input().split()
    #print(test)
    T_time = int(test[0])
    #print(T_time)
    T_minutes = int(test[1])
    #print(T_minutes)
    T_All = T_time * 60 + T_minutes
    #print(T_All)
    train += str(T_All)

print(train)

#print(int(train[n+3] + train[n+4] + train[n+5]))

for _ in range(n):
    if int(train[n+3] + train[n+4] + train[n+5]) < 539:
        #print('YES')
        kotae = int(train[n+3] + train[n+4] + train[n+5]) - MoveA
        break
    else:
        n -= 3

#print(kotae - MoveA)
a = kotae // 60
b = (kotae - a * 60)
#print(a, b)

if len(str(a)) == 1 and len(str(b)) == 1:
    print(f'0{a}:0{b}')
elif len(str(a)) == 1:
    print(f'0{a}:{b}')
elif len(str(b)) == 1:
    print(f'{a}:0{b}')
else:
    print(f'({a}:{b}')
#if int(train[N * 2 - 2]) * 60 + (MoveB_C) < 539: