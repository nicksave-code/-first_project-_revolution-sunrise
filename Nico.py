print('Escriba su nombre')
how = input()
Good = len(how)
print("¿Desea saber cuántas letras tiene su nombre?")
log = input()
#Espacio
Oh = "No"
Yes = "Sí"
Aviso = "Si"
if Yes == log: 
    print( "Su nombre tiene " + str(Good) + " letras.")    
elif Oh == log:
    print("Como usted mande")
else:
    print("No comprendí")
#Después
print("Escriba x")
x = input()
print("Escriba y")
y = input()
MouX = str(int(x))
MouY = str(int(y))
print(str(int(MouX)/int(MouY)))