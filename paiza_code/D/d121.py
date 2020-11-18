word_L = []
word = input()
word_L += word



def A(word_L, word):
    if word[0] == 'A':
        return f'R{word_L[1]}{word_L[2]}'
    return word



print(A(word_L, word))