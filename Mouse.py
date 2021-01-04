Math = 0
while 2 != Math: #2020 
   Math = int(Math)+1
   Two = int(Math)
   Three = int(Math)+1
   Buu = Two * Three
   print( "(" + str(Two) + " x " + str(Three) + ")" + " = " + str(Buu))
   if Two == 2: #2020
      break
if Math == (500):
   print("Todo listo")
#Math = (1x2) + (2x3) + (3x4) + ...... + (99x100)
#Signo "*" = Multiplicación
print("¿Qué deseas realizar?")
Duck = input()
while Duck == "operación":
   print("¿Qué tipo deseas?")
   
   Bu = input()
   while Bu == "exp":
      print("Base:")
      Base = int(input())
      print("Exponente: ")
      Up = input()
      print(str(Base) + " ^ " + str(Up) + " = " + str(int(Base)**int(Up)))
   while Bu == "function":
      print("f(x) = x+2")
      print("x = ")
      x = int(input())
      print("f(" + str(x) + ") = "+ str(x+2))
print("Adiós")
#solucionar después
      
