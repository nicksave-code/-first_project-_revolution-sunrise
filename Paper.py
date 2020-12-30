print('escriba su nombre')
nombre = input()
print ("Escriba su contraseña")
contraseña = input()
print("¿Cuál es tu edad?")
Edad = int(input())
if nombre == 'Alice':
    print ('Hola, Alice')
while contraseña != "pez espada":
    print("Vuelve a escribir")
    contraseña = input()
if Edad > 17:
    print( str(Edad) + " años " + "diviértete")
if Edad < 17:
    print("Uh, " + "¡ " + str(Edad) + " años !, aun una pequeña.")
if contraseña == 'pez espada':
    print ('Acceso concedido.')
