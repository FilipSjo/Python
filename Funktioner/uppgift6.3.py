
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

def fixa_matte(val):
matte = {
    '+' : (lambda var1, var2: var1 + var2),
    '-' : (lambda var1, var2: var1 - var2),
    '*' : (lambda var1, var2: var1 * var2), 
    '%' : (lambda var1, var2: var1 % var2),
    '/' : (lambda var1, var2: var1 / var2)
return matt[(val)]
}

lista = inmatning()
print_lambda(lista[0], lista[1], matte[lista[2]])

