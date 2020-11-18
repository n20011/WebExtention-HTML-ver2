N, nunber = map(int, input().split())
Base_N = bin(nunber)

#print(N, Base_N)

for _ in range(N):
    place_N = int(input())
    #print(place_N)
    print(Base_N[place_N * -1])