import pandas as pd
import numpy as np
def inmatning():
    lista_att_markera = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))
    element_i_listan = int(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    """val = str.upper(input("Vad vill du göra med talen? Ange: +, -, *, %, eller / \n"))"""
    lista = [lista_att_markera, element_i_listan]
    print(f"Du valde att placera markören på: {lista}")
    return lista
#har sparat input i en lista, borde går att göra en loop som går igenom listan och ersätter ett tecken med O eller X
lista1 = ['-','-','-']
lista2 = ['-','-','-']
lista3 = ['-','-','-']

df = pd.DataFrame(list(zip(lista1, lista2, lista3)), columns =['A', 'B', 'C']) 
#undersöker sen om det är bättre att använda for-loop för att lösa problemet
"""def placera_marker(lista, spelplan):
    for element in lista:"""

#kör en lista istället? den verkar inte vilja ersätta mellanrum, kolla efter alternativ     

def placera_marker(listan):
    df2 = df.replace([listan[0], listan[1], 'X'])
    
    return df2
 
#vi ska returnera en lista som ska läggas in i en ny dataframe?
#hej = df.replace({'A':{1:'X'}})
#print(replace_for_x('A', 3))
print(df)
runda1 = placera_marker()
print(runda1)

