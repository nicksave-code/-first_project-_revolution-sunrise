print("Welcome to Sunrise Education")
print("¿Deseas ver el mundo de un modo maravilloso?")
print("Todo es posible, solo usemos las áreas más divertidas.\n")
Name = input("¿Cómo desea que le llame?  ")
print("Uhm, dejeme ver la base de datos...\n")
#Function begin
def search_name(word):
    if word == "Sandra" or word == "sandra":
        global Name
        Name = "Sandra"
        print("Señorita Sandra, ¿cómo le va?")
    else:
        print("No te recuerdo... \nLo siento")
#Function end
search_name(Name)