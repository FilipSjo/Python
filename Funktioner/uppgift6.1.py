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
def inmatning():
    tal1, tal2 = int(input("Ange ett tal \n")), int(input("Nästa tal \n"))
    val = str(input("Vad vill du göra med talen? Ange: +, -, *, %, eller / \n"))
    lista = [tal1, tal2, val]
    return lista


lambda_plus = lambda var1, var2: var1 + var2
lambda_minus = lambda var1, var2: var1 - var2
lambda_multi = lambda var1, var2: var1 * var2     
lambda_divis = lambda var1, var2: var1 / var2
lambda_mod = lambda var1, var2: var1 % var2
def print_lambda(v1, v2, val):
    print(f"{v1} och {v2} ger: {val(v1, v2)}")

matte = {
    '+' : lambda_plus,
    '-' : lambda_minus,
    '*' : lambda_multi,
    '%' : lambda_mod,
    '/' : lambda_divis
}

lista = inmatning()
print_lambda(lista[0], lista[1], matte[lista[2]])


#tal1, tal2, val = inmatning()
#print(tal1)
#print(val)
#print_lambda(tal1, tal2, val)
