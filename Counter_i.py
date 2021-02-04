#math conunter for i.
#Welcome to the auto!
Number = 0
Number = input()
while Number == "Solve i":
 while True:
  Number = input()
  if Number != "Thanks":
    Number = int(Number)
  if Number == "Thanks":
    break
  x = 4
  y = 4
  z = 0
  a = 1
  b = 0    
  c = 1
  while True: 
   b = b + 1 #Ok?
   #Is a counter math...
   d = int(y)*b
   if Number >= c and Number <= d:
    break
   c = c + 4
  print("Your " + str(c) + " <= " + str(Number) + " <= " + str(d))
  One = " is i"
  Two = " is -1"
  Three = " is -i"
  Four = " is 1"
  d = d - Number
  docGo = 3 - d
  if docGo == 0:
    print("I^ " + str(Number) + One)
  if docGo == 1:
    print("I^ " + str(Number) + Two)
  if docGo == 2:
    print("I^ " + str(Number) + Three)
  if docGo == 3:
    print("I^ " + str(Number) + Four)        
print("Goodbye")
#print(str(c) + " >= " + str(Number) + " >= " + str(d))

#Good work!