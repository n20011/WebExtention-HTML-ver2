N = int(input())
word = input()
box = []



def search(word):
    Log_word = input()
    if word in Log_word:
        return Log_word
    return None



for _ in range(N):
    box.append(search(word))



count = 0
for n in range(N):
    if box[n] != None:
            print(box[n])
    else:
        count += 1



if count == N:
    print(None)