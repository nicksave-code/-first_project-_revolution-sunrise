word = str(input())
while word != "bye":
    word = " " + word + " "
    point = "."
    up_line = "-"
    with_up = len(word) #len word with up line
    up_lineNew = up_line*with_up
    print("  ")
    print(point + up_lineNew + point)
    print("|" + word+ "|")
    print("'" + up_lineNew + "'")
    word = str(input())