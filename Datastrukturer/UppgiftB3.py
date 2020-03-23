
pers1 = {"Namn" : input("Ange namn för person 1: "), "Ålder" : int(input("Ange ålder för person 1: ")), "Skostorlek" : int(input("Ange skostorlek för person 1: "))}




#print("Namn: ", pers1[0], "\n" "Ålder: ", pers1[1], "\n" "Skostorlek: ", pers1[2])

#test = input("Ange 0 för namn, 1 för ålder eller 2 för skonummer: ")

pers1_lst =[pers1.values()]

print(pers1_lst)
#print(pers1[test])
print(pers1["Skostorlek"])