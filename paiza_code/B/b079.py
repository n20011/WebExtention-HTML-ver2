s, t = input().split()

L_st = len(s + t)

S_box = []
for S in s:
    S_box += S

T_box = []
for T in t:
    T_box += T

ST_box = S_box + T_box
TS_box = T_box + S_box



#辞書a-z
def DICT(n):
    box = {
        'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 
        'f':6, 'g':7, 'h':8, 'i':9, 'j':10,
        'k':11, 'l':12, 'm':13, 'n':14, 'o':15,
        'p':16, 'q':17, 'r':18, 's':19, 't':20,
        'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26
    }
    return box[n]




INT_1box = []
for n in range(L_st):
    INT_1box.append(DICT(ST_box[n]))


nn = 0
for _ in range(L_st -1):
    nn += 1
    N = 0
    INT_2box = []
    for _ in range(L_st - nn):
        I_BOX = INT_1box[N] + INT_1box[N+1]
        if I_BOX >= 101:
            I_BOX -= 101
            INT_2box.append(I_BOX)
            N += 1
        else:
            INT_2box.append(I_BOX)
            N += 1
        #print(INT_2box)
            
    INT_1box = INT_2box

#print(INT_2box[0])





INT_3box = []
for n in range(L_st):
    INT_3box.append(DICT(TS_box[n]))


nn = 0
for _ in range(L_st -1):
    nn += 1
    N = 0
    INT_4box = []
    for _ in range(L_st - nn):
        I_BOX = INT_3box[N] + INT_3box[N+1]
        if I_BOX >= 101:
            I_BOX -= 101
            INT_4box.append(I_BOX)
            N += 1
        else:
            INT_4box.append(I_BOX)
            N += 1
        #print(INT_4box)
            
    INT_3box = INT_4box

if INT_2box[0] >= INT_4box[0]:
    print(INT_2box[0])
else:
    print(INT_4box[0])