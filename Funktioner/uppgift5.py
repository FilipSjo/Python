from random import seed
from random import randint


seed(1) # bör funka utan seed, seeden gör att man kan återskapa siffer-sekvensen
#skapa lista
lista = []
for x in range(20):
    value = randint(0, 100)
    lista.append(value)

#print(lista)
def hel_koll():
    x = True
    inmatning = str(input("Ange ett heltal: \n"))
    while x == True:
        if inmatning.isdecimal() == False:
            inmatning = str(input("FEL, ange ett heltal: \n"))
        else:
            print(f"{inmatning} är ett tal, vi fortsätter")
            x = False
    return inmatning


inmatning2 = hel_koll()
inmatning = int(inmatning2)

#while x == True:
        #inmatning = int(input("Ange ett heltal eller avsluta genom att mata in 00, \n"))
        #if inmatning == 00:
        #    x = False
even = []
uneven = []
for nummer in lista:
    if nummer > inmatning and nummer % 2 !=0:
        uneven.append(nummer)
    elif nummer < inmatning and nummer % 2 ==0:
        even.append(nummer)
print(lista)
print(f"{inmatning} är mindre än {uneven}")
print(f"{even} är listan med alla jämna tal större än {inmatning}")