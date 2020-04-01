pers1 = {input("Ange namn för person 1: ") : int(input("Ange ålder för person 1: ")), int(input("Ange skostorlek för person 1: "))}

pers1sort = sorted(pers1.values())
pers1sort2 = sorted(pers1.keys())
print(pers1sort)
print(pers1sort2)
#pers1sort = sorted(pers1.items())
#pers1sort2 = sorted(pers1.items(),key=lambda x: x[1])

#print(pers1sort)

#print(pers1sort2)
#print(pers1.sort(key=operator.itemgetter(1)))