message = input()



def leet(word):
    for W in range(len(word) + 1):
        message_L = list(message)
        mL_l_word = []
        dict_leet = {
            'A' : '4',
            'E' : '3',
            'G' : '6',
            'I' : '1',
            'O' : '0',
            'S' : '5',
            'Z' : '2'
        }

        for W in message_L:
            if W in ['A', 'E', 'G', 'I', 'O', 'S', 'Z']:
                mL_l_word += [dict_leet[W]]
            else:
                mL_l_word += [W]

    return mL_l_word



def organize(MS):
    box = ''
    for last in MS:
        box += last
    
    return box



print(organize(leet(message)))