x_1, y_1, p_1 = input().split()
X_1, Y_1, P_1 = int(x_1), int(y_1), int(p_1)
x_2, y_2, p_2 = input().split()
X_2, Y_2, P_2 = int(x_2), int(y_2), int(p_2)

# p / (x * y)
xyp1 = P_1 / (X_1 * Y_1)
xyp2 = P_2 / (X_2 * Y_2)
#print(xyp1, xyp2)



if xyp1 > xyp2:
    print(f'{X_2} {Y_2} {P_2}')
    
elif xyp2 > xyp1:
    print(f'{X_1} {Y_1} {P_1}')
    
else:
    print('DRAW')