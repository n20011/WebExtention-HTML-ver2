n = int(input())



def Elevator(floor_N, floor_D):
    if floor_N >= floor_D:
        return floor_N - floor_D
    return floor_D - floor_N



floor_D = 1
count = 0
for _ in range(n):
    floor_N = int(input())
    count += Elevator(floor_N, floor_D)
    floor_D = floor_N

print(count)