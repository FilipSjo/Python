import pandas as pd
import numpy as np

lista1 = [' ',' ',' ']
lista2 = [' ',' ',' ']
lista3 = [' ',' ',' ']
df = pd.DataFrame({'A':lista1, 'B':lista2, 'C':lista3})

lista_att_markera = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))

element_i_listan = int(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    
lista = [lista_att_markera, element_i_listan]
#man kanske kan köra en append till en lista här för att se vilka drag som har gjorts


print(df)


print(lista[0])