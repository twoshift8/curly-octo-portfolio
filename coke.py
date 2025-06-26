
def vend():
    cost = 50
    while 0 < cost <= 50:
        coin = int(input("Amount Due: "+ str(cost) + "\nInsert Coin: "))
        if coin in [25, 10, 5]:
            cost -= coin
        if cost <= 0:
            print("Change Owed:", abs(cost))


if __name__ == "__main__":
    vend()

#submit50 cs50/problems/2022/python/coke
