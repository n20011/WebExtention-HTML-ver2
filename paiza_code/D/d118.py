word = input()
nunber = int(input())



def S_H(word, nunber):
    S = 1926
    H = 1989
    if word == 'S':
        return (S + nunber) - 1
    return (H + nunber) - 1



print(S_H(word, nunber))