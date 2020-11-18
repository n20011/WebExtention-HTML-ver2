N = int(input())



def es(word_box):
    if word_box[-1] == 's' or word_box[-1] == 'o' or word_box[-1] == 'x':
        return True
    
    if word_box[-2:] == 'sh' or word_box[-2:] == 'ch':
        return True
    
    return False



def ves(word_box):
    if word_box[-1] == 'f' or word_box[-2:] == 'fe':
        return True
        
    return False



def ies(word_box):
    if word_box[-1] == 'y':
        if word_box[-2] != 'a' and word_box[-2] != 'i' and word_box[-2] != 'u' and word_box[-2] != 'e' and word_box[-2] != 'o':
            return True
    
    return False


for _ in range(N):
    word_box = input()
    #print(word_box[-2:])
    #print(word_box.rstrip(word_box[-2:]))
    #print(word_box[-2])
    if es(word_box):
        print(f'{word_box}es')
    

    elif ves(word_box):
        if word_box[-1] == 'f':
            print(f'{word_box.rstrip(word_box[-1])}ves')
        else:
            print(f'{word_box.rstrip(word_box[-2:])}ves')
    

    elif ies(word_box):
        print(f'{word_box.rstrip(word_box[-1])}ies')
    

    else:
        print(f'{word_box}s')