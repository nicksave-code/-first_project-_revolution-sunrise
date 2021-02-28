Algoritmo sin_titulo 
	Escribir "Digite dos números"
	Leer Numero1
	Leer Numero2
	Suma<-Numero1 + Numero2
	Escribir  "Escribe entrada"
	Leer Entrada
	 Segun Entrada Hacer
		2:
			Escribir "Dos es igual a 2"
		20:
			Escribir "Veinte es igual a 20"
		15:
			Escribir "Quince es igual a 15"
		De Otro Modo:
			Escribir "Dos"
	Fin Segun
	Escribir "El resultado de la suma es: " Suma
	n<-0
	Repetir
		n<- n + 1
		Escribir n
	Hasta Que n == 20
FinAlgoritmo
