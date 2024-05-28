def printArguments(x, y, z):
    print("x=%d, y=%d, z=%d" % (x, y, z))
    sum = x + y + z
    print("x+y+z=%d" % sum)

printArguments(10, 20, 30)
printArguments(x=300, y=100, z=200)
printArguments(x=3000, y=1000, z=2000)
