print("Hola, ¿cómo te llamas?")
Name = input()
print("Hello " + Name + ", how are you?")
status = input()
if status == "Good" or status == "good" or status == "Bien" or status == "bien":
    print("Me encanta escuchar eso, tengo algo para ti.")
elif status == "Bored" or status == "bored" or status == "Aburrido" or status == "aburrido" or status == "Aburrida" or status == "aburrida":
    print("Has preparado todo para hoy, tal vez falte algo")
    print("¿Deseas que te muestre el trabajo de hoy?")
    answer = input()
    if answer == "Yes" or answer == "yes" or answer == "Sí" or answer == "sí" or answer == "Si" or answer == "si":
        if answer == "Si" or answer == "si":
            print("Esa ortografía por favor.")
        print("Hoy tienes que sonreír por qué de la noche a la mañana has convertido el humo en agua, juu.\nさよなら")