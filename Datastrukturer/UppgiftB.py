pers01, pers02, pers03 = str(input("Ange namn för person1: ")), int(input("Ange ålder för person1: ")), int(input("Ange skostorlek för person1: "))

pers01_set = {pers01, pers02, pers03}

pers01_str = str(pers01_set.copy)

print(pers01_set)
print(pers01_str)