def coinChange(coinList, amount):
    toPay = amount
    coinList.sort()
    index = -1
    ans = []
    while True:
        coinValue = coinList[index]
        if toPay == 0:
            break
        elif toPay >= coinValue:
            ans.append(coinValue)
            toPay = toPay - coinValue
        elif toPay < coinValue:
            index -= 1

    print(ans)
    print("Total number of coins: ", len(ans))


amount = 47
coinList = [1, 2, 5, 10]

coinChange(coinList, amount)
