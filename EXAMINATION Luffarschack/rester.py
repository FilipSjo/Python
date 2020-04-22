import pandas as pd
import numpy as np
"""lista1 = ['-','-','-']
lista2 = ['-','-','-']
lista3 = ['-','-','-']"""
#df = pd.DataFrame({'A':lista1, 'B':lista2, 'C':lista3})#är det något speciellt med hur denna har skapats? se parenteserna

dict_med_listor = {
    'A' : [' ', ' ', ' ']
    'B' : [' ', ' ', ' ']
    'C' : [' ', ' ', ' ']
}

def inmatning():
    lista_att_markera = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))
    element_i_listan = str(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    """val = str.upper(input("Vad vill du göra med talen? Ange: +, -, *, %, eller / \n"))"""
    lista = [lista_att_markera, element_i_listan]
    print(f"Du valde att placera markören på: {lista}")
    return lista
#kör på lista som sätts ihop till df istället för att ändra i dataframen
def placera_marker(listan):
   if lista[0] = 'A':
    lista_med_drag = lista1[listan[1]] = 'X'
    
    return df2

hej = inmatning()

print(hej[-1])
print(hej[0])
