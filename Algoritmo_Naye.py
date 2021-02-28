#Algoritmo para Valor Absoluto
print("Ingrese un número")
Abs_num = int(input())
while True:
    if Abs_num < 0:
     Abs_num = (-1)*int(Abs_num)
     print("Su valor absoluto es: " + str(Abs_num))
    elif Abs_num > -1:
        print("Su valor absoluto es: " + str(Abs_num))
    else:
        break
    Abs_num = int(input())
#finAlgoritmo