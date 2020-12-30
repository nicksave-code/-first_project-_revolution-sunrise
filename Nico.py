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
print("6.5 = ")
print("a) 20")
print("b) 30")
Cow = "b"
Dos = input()
if Cow == Dos:
    print("¡Muy bien!")
else:
        print("Lo siento")

print('¿Cuál es la base?')
Base = input()
print("¿Cuál es el exponente")
Exp = input()
print("Beep boop")
print(str(Base) + " ^ " + str(Exp) + " es igual a: " + str(int(Base)**int(Exp)))   