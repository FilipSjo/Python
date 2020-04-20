import pandas as pd
import numpy as np


def inmatning():
    lista_att_markera = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))
    element_i_listan = int(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    """val = str.upper(input("Vad vill du göra med talen? Ange: +, -, *, %, eller / \n"))"""
    lista = [lista_att_markera, element_i_listan]
    return lista

lista1 = [' ',' ',' ']
lista2 = [' ',' ',' ']
lista3 = [' ',' ',' ']

def print_lambda(v1, v2, val):
    print(f"{v1} och {v2} ger: {val(v1, v2)}")

dict_med_listor = {
    'A' : lista1
    'B' : lista2
    'C' : lista3
}

lista = inmatning()
print_lambda(lista[0], lista[1], matte[lista[2]])

def ta_input3(lista_att_markera, element):

    for element in lista_att_markera:
     print(f"\n{element}")   

df = pd.DataFrame({'A':lista1, 'B':lista2, 'C':lista3})

print(f"Här kommer listorna ihopsatta till en Spelplan: \n {df}")
"""ta_input3(ta_input(), ta_input2())"""
#gör funkltion som tar original-listorna och itererar på dom i en loop, med inmatning osv
#som går 2 steg, ett för spelare X och ett för spelare 0:
#efter det så sparas brädet i en ny variabel och man kan välja att fortsätta?


