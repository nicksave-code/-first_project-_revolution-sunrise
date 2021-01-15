print("Primer número")
Number1 = int(input())
print("Segundo número")
Number2 = int(input())
while Number1 != "Salir":
  if Number1 < Number2:
    print(str(Number1) + " es menor que " + str(Number2))
    print("....")
    if Number1 == 0:
      print("0 " + "es menor que " + Number2)
    
  elif Number1 > Number2:
    print(str(Number1) + " es mayor que " + str(Number2))
    print("....")
  else:
   print("Vuelva a escribir")
  print("Primer número")
  Number1 = int(input())
  print("Segundo número")
  Number2 = int(input())
  