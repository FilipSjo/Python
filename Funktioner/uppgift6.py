#1. Skapa ett program som frågar användaren efter två tal och ett av de fyra
#räknesätten (+, -, *, /) och sedan returnerar resultatet som blir om man
#tillämpar räknesättet på dessa två.

#2. Efter att du testkört programmet, bygg ut det så att det även kan hantera
#modulus-operatorn (%)

#funktion addition

#funktion subtraktion

#funktion multiplikation

#funktion Division

#funktion modulus (%)

tal1, tal2 = int(input("Ange ett tal \n")), int(input("Nästa tal \n"))


plus = lambda var1, var2: var1 + var2
minus = lambda var1, var2: var1 - var2
multi = lambda var1, var2: var1 * var2
divis = lambda var1, var2: var1 / var2


val = str(input("Vad vill du göra med talen? Ange: +, -, *, eller / \n"))

if val == "+":
    print(plus(tal1, tal2))    
elif val == "-":
    print(minus(tal1, tal2))
elif val == "*":
    print(multi(tal1, tal2))
elif val == "/":
    print(divis(tal1, tal2))



