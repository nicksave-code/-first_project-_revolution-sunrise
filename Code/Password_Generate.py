import random
q = 0
r = 0
a = ["S", "M", "K", "f", "R", "A", "x", "d", "l", "B", "a", "Z", "p", "l", "O", "Q", "M", "F", "A", "s", "x", "r", "j", "u"]
b = ["2", "h", "z", "P", "k", "g", "a"]
a = random.choice(a)
b = random.choice(b)
r = str(random.randint(1, 9))
print(a, r, b, sep="")