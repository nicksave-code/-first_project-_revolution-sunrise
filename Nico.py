print('Escriba su nombre')
how = input()
Good = len(how)
print("¿Desea saber cuántas letras tiene su nombre?")
log = input()
#Espacio
Oh = "No"
Yes = "Sí"
while Yes != log:
  print("De nuevo")
if Yes == log: 
  print( "Su nombre tiene " + str(Good) + " letras.")    
elif Oh == log:
    print("Como usted mande")
#Congratulations
#Después
print("Escriba x")
x = input()
print("Escriba y")
y = input()
MouX = str(int(x))
MouY = str(int(y))
print(str(int(MouX)/int(MouY)))