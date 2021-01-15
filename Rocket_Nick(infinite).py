#Num = 2
#while Num != 3:
#    print("Más allá del universo")
#Inicio = 0
#Doc = 0
#while Doc != 100:
# Doc = Doc + 1
# Inicio = Inicio + Doc
#print(Inicio) 
print("Ingresa M:")
Let_st = int(input())
print("Ingresa N:")
Let_nd = int(input())
while Let_st < 100:
 if Let_st > 3 and Let_st < 6:    
  Let_st = int(Let_st)+1
 if Let_st >= 0 and Let_st < 6: 
     if Let_nd > -2 and Let_nd < 1:
        Let_nd = Let_nd+1
        print("( " + str(Let_st) + " ; " + str(Let_nd) + " )") 
 else:
    break
