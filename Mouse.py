print("Welcome to NiCo Sunrise")
print("Username")
name = input()
print ("Enter your password")
password = input()
print ('Hello, ' + name)
while password != "laniñajuju":
    print("Contraseña denied")
    password = input()
if password == '01/01/2003':
    print("Welcome to your account")
print("¿Cuál es tu nombre?")
how = input()
print("Un gusto " + how)
Good = len(how)
print("¿Desea saber cuántas letras tiene su nombre?")
log = input()
#Espacio
Oh = "No"
Yes = "Sí"
while Yes != log:
  print("De nuevo")
  log = input()
  #Bucle infinito error(Yes!)
if Yes == log: 
  print( "Su nombre tiene " + str(Good) + " letras.")    
elif Oh == log:
    print("Como usted mande")
#Congratulations
#Después
print("Una división")
print("Escriba x")
x = input()
print("Escriba y")
y = input()
MouX = str(int(x))
MouY = str(int(y))
print(str(int(MouX)/int(MouY)))
#After
Math = 0
print("En una operación (1.2) + (2.3) + (3.4) + ...... + (x.(x+1)), ¿A qué número desea sustituir la variable x?")
Number = int(input())
while Number != Math: #2020 
   Math = int(Math)+1
   Two = int(Math)
   Three = int(Math)+1
   Buu = Two * Three
   print( "(" + str(Two) + " x " + str(Three) + ")" + " = " + str(Buu))
   if Two == Number: #2020
      break
if Math == (Number):
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
      print("¿De nuevo?")
      Answer = input()
      if Answer == "Sí":
       continue
      else:
       break    
   while Bu == "function":
      print("f(x) = x+2")
      print("x = ")
      x = int(input())
      print("f(" + str(x) + ") = "+ str(x+2))
      print("¿Continuar con la función?")
      B_on = input()
      if  B_on == "Sí":
       continue
      else:
       break
   if Bu == "Ninguna": 
       break    
print("Adiós")
#solucionar después