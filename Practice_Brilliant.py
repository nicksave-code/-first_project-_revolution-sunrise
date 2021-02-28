#Practice brilliant
d = ["beard", "brown hair", "smiling", "blue hair", "long hair", "black hair", "glasses"]
m = int(input())
def ans(b): 
    global a
    a = d[b-1]
    return print(a)
if m == 1:
    ans(m)
    print("Is A")
elif m == 2:
    print("Is B")
elif m == 3:
    j = int(input())
    if j == 4:
        print("Is C")
    elif j == 5:
        print("Is D")
    elif j == 6:
        j = int(input())
        if j == 7:
            print("Is E")
        else:
            print("Is F")
    else:
        print("Is G")
else:
    print("Is H")