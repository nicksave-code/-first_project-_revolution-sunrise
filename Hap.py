import sys
import random
myGame = input("Para comenzar ")
win = 0
loser = 0
equal = 0
while myGame != "Fin":
    a = random.randint(1,3)
    if a == 1:
     b = "Piedra"
    if a == 2:
     b = "Papel"
    if a == 3:
     b = "Tijera"
    if myGame == "Tijera" and a == 1:
     print(b + " vs " + myGame)
     print("Tú perdiste")
     loser = int(loser) + 1 
    if myGame == "Tijera" and a == 2:
     print(b + " vs " + myGame)
     print("Tú ganaste")
     win = int(win) + 1
    if myGame == "Tijera" and a == 3:
     print(b + " vs " + myGame)
     print("Quedaron iguales")
     equal = int(equal) + 1
    if myGame == "Papel" and a == 1:
     print(b + " vs " + myGame)
     print("Tú perdiste")
     loser = int(loser) + 1
    if myGame == "Papel" and a == 2:
     print(b + " vs " + myGame)
     print("Uf, hoja con hoja, es una igualdad.")
     equal = int(equal) + 1
    if myGame == "Papel" and a == 3:
     print(b + " vs " + myGame)
     print("Oh no, una tijera, ¡corre!")
     loser = int(loser) + 1
    if myGame == "Piedra" and a == 1:
     print(b + " vs " + myGame)
     print("Son hermanos, oye")
     equal = int(equal) + 1
    if myGame == "Piedra" and a == 2:
     print(b + " vs " + myGame)
     print("Pobre hoja, adiós; tú ganas.")
     win = int(win) + 1
    if myGame == "Piedra" and a == 3:
     print(b + " vs " + myGame)
     print("¿Y ahora?, ¿Qué sucederá con el papel?")
     win = int(win) + 1
    if myGame == "Puntaje":
        print("Win: " + str(win) + " Loser: " + str(loser) + " Equal: " + str(equal) + " ...")
    print("------------------------")
    myGame = input("Yo escojo ")
    if myGame == "New":
        win = 0
        loser = 0
        equal = 0