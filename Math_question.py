#Exercise Full Funny!
#Don't me give up
print("Enter the number juuuu")
c = 0
while c != 1:
 def par(x):
    try: 
        y = int(x)%2
        if y == 1:
            global a
            a = int(x)*3+1
            print(a)
        elif y == 0:
            global b
            b = int(x)/2
            print(int(b))
    except:
        print("Error")
 x = input()
 par(x)
#Pretty code, congratulations! now Chapter 4...