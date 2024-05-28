def localTrade():
    global price  
    salePrice = price * 1.2
    print(price, salePrice)
    price = 2000
    salePrice = price * 1.2
    print(price, salePrice)
    
price = 1000
localTrade()
print(price)  
