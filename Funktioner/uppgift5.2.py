from random import seed
from random import randint

# bör funka utan seed, seeden gör att man kan återskapa siffer-sekvensen
#skapa lista
lista = []
antal_tal = int(input("ange antal tal i listan: \n"))
range_tal = int(input("ange högsta talet: \n"))
for x in range(antal_tal):
    value = randint(0, range_tal)
    lista.append(value)

print(lista)