#försökte lägga in allt i funktioner och då blev det jobbigt med globala och lokala variabler
#det funkade innan jag gjorde "ta input", "sort_small_and_large" samt "skapa_lista"

def skapa_lista():
    x = True
    lista = []
    print("Ange hur många tal du vill.")
    while x == True:
  
        inmatning = int(input("Ange ett heltal eller avsluta genom att mata in 00, \n"))
        if inmatning == 00:
            x = False
        else:
            lista.append(inmatning)
    return lista

def ta_input():
    print(lista)
    inpt = int(input("vänligen välj ett tal i listan ifrån listan: "))
    #plist = [inpt]
    return inpt

def sort_small_and_large(lista, plist):
    smaller = []
    larger = []
    plist = []
    plist.append(inpt)
    for Number in lista: #(förutom p)
        if Number < inpt:
            smaller.append(Number)
        elif Number > inpt:
            larger.append(Number)
    return smaller, larger, plist

def sorterat(list1, list2):
        if (len(list1) > 1 or len(list2) > 1):
            list1.sort()
            list2.sort()
        return list1, list2

def addera(list1, list3, list2):

    return list1 + plist + list2

lista = skapa_lista()
inpt = ta_input()
print(inpt)
smaller, larger, plist = sort_small_and_large(lista, inpt)
print(smaller)
print(larger)
print(plist)
sort_small, sort_large = sorterat(smaller, larger)
print(sort_small)
print(sort_large)
resultat = addera(smaller, plist, larger)
print(resultat)
#print(sort1)
#return sorted_lista
#sorted_list = smaller + p + larger
#jaja = sorterat(smaller, larger)
#ja = addera(smaller, p, larger)
#print(ja)
#print(jaja)
