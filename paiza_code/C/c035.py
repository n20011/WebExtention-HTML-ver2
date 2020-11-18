n = int(input())



def score(sE, sM, sS, sN, sH):
    if sE + sM + sS + sN + sH >= 350:
        return True
    return False



def L_S(LS):
    if LS == 'l':
        return 'L'
    return 'S'



def L(sN, sH):
    if sN + sH >= 160:
        return True
    return False



def S(sM, sS):
    if sM + sS >= 160:
        return True
    return False

#L=文系 S=理系
#E英語　M数学　S理科　N国語　H地歴
count = 0
for _ in range(n):
    LS, s_E, s_M, s_S, s_N, s_H = input().split()
    LS, sE, sM, sS, sN, sH = LS, int(s_E), int(s_M), int(s_S), int(s_N), int(s_H)
    
    if score(sE, sM, sS, sN, sH):

        if L_S(LS) == 'L':
            if L(sN, sH):
                count += 1

        elif S(sM, sS):
            count += 1
            
print(count)