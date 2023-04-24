cost = 50
while cost > 0:
    print("Нужная сумма:",cost)
    coin = int(input("Вставьте монету: "))
    if (coin == 50) or (coin == 20) or (coin == 10) or (coin == 5):
        cost = cost - coin
        print("Ваша сдача:", abs(cost))
