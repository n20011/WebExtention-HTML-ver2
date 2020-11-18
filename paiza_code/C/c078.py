n, c_1, c_2 = input().split()
N, C_1, C_2 = int(n), int(c_1), int(c_2)



def down(C_1, price):
    if C_1 >= price:
        return True
    return False



def up(C_2, price):
    if C_2 <= price:
        return True
    return False



def pay_off(L_price, stock, Money):
    return (L_price * stock) + Money



Money = 0
stock = 0
for _ in range(N - 1):
    price = int(input())
    if down(C_1, price):
        Money -= price
        stock += 1
    
    elif up(C_2, price):
        Money += price * stock
        stock = 0

L_price = int(input())
print(pay_off(L_price, stock, Money))