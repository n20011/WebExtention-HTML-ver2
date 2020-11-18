#タテ
a_s = [a_1, a_2, a_3, a_4, a_5] = input()
b_s = [b_1, b_2, b_3, b_4, b_5] = input()
c_s = [c_1, c_2, c_3, c_4, c_5] = input()
d_s = [d_1, d_2, d_3, d_4, d_5] = input()
e_s = [e_1, e_2, e_3, e_4, e_5] = input()
box_s = [a_s, b_s, c_s, d_s, e_s]

#ヨコ
a_v = [a_1, b_1, c_1, d_1, e_1]
b_v = [a_2, b_2, c_2, d_2, e_2]
c_v = [a_3, b_3, c_3, d_3, e_3]
d_v = [a_4, b_4, c_4, d_4, e_4]
e_v = [a_5, b_5, c_5, d_5, e_5]
box_v = [a_v, b_v, c_v, d_v, e_v]

#ナナメ
a_d = [a_1, b_2, c_3, d_4, e_5]
b_d = [a_5, b_4, c_3, d_2, e_1]
box_d = [a_d, b_d]



def side_G(box_s):
    for n in range(5):
        if box_s[n] == 'OOOOO':
            return [True, 'O']
        
        if box_s[n] == 'XXXXX':
            return [True, 'X']
    
    return [False]



def vertical_G(box_v):
    for n in range(5):
        if ''.join(box_v[n]) == 'OOOOO':
            return [True, 'O']
        
        if ''.join(box_v[n]) == 'XXXXX':
            return [True, 'X']
        
    return [False]



def diagonal_G(box_d):
    for n in range(2):
        if ''.join(box_d[n]) == 'OOOOO':
            return [True, 'O']

        if ''.join(box_d[n]) == 'XXXXX':
            return [True, 'X']
    
    return [False]



if side_G(box_s)[0]:
    print(side_G(box_s)[1])

elif vertical_G(box_v)[0]:
    print(vertical_G(box_v)[1])

elif diagonal_G(box_d)[0]:
    print(diagonal_G(box_d)[1])

else:
    print('D')