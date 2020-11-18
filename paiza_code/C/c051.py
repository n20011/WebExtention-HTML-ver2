a, b, c, d = input().split()



box = [a, b, c, d]

no1 = sorted(box)[-1]
no2 = sorted(box)[-2]
no3 = sorted(box)[-3]
no4 = sorted(box)[-4]



print(int(no1 + no3) + int(no2 + no4))