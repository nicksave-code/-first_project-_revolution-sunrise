s = int(input())
b = float(175937.79)
while s != 2030:
    if s > 0 and s < -2:
        word = " bitcoin"
    else: 
        word = " bitcoins"
    result = s*b
    print(str(s) + " soles es igual a " + str("%.2f" % result) + word)
    s = int(input())
    print() 