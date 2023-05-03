n = 1260

count = 0
coincount = 0

coin_type = [500,100,50,10]

for coin in coin_type:
    coincount = n // coin
    count += coincount
    n %= coin
    print(coin, coincount)
    if(n==0) : break
    """ print(coin,coincount) """

