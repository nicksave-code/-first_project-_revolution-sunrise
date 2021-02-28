#Num = 2
#while Num != 3:
#    print("Más allá del universo")
#Inicio = 0
#Doc = 0
#while Doc != 100:
# Doc = Doc + 1
# Inicio = Inicio + Doc
#print(Inicio) 
#print("Ingresa M:")
#One = int(input())
#print("Ingresa N:")
#Two = int(input())
#while One < 100:
 #if One > 3 and One < 6:    
  #if One >= 0 and One < 6: 
 #if Two > -2 and Two < 1:
   # Two = Two+1
   # print("( " + str(Two) + " ; " + str(One) + " )") 
 #else:
   # break

#Suma de impares consecutivos...
import random
#One = 0
#while True:
# if One == 20:
#  break
# print(One)
# One = One + 1
#for Num in[2, 3, 6]:
# Num = 0
Var = random.randint(1, 5)
Guess = Var
print(Guess)
Doc = input()
while Doc != Var:
  print("Sorry!")
  print("Is " + str(Guess))
  Doc = input()
print("Very good!")
#Mind error!!
"""
 #abs in a nutshell
 x = int(input())
 if x < 0:
  x = (-1)(int(x)) 
 if x > 0:
  x = (int(x))
 print(x)
"""