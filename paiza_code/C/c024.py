codnunber = int(input())


def SETING(nunber, ):
    box = []
    b_1 = 0
    b_2 = 0

    for _ in range(nunber):
        box = input().split()

        if box[0] == 'SET':
            if box[1] == '1':
                b_1 = int(box[2])
            else:
                b_2 = int(box[2])
        
        elif box[0] == 'ADD':
            b_2 = b_1 + int(box[1])

        else:
            b_2 = b_1 - int(box[1])
    

    return print(b_1, b_2)



SETING(nunber)