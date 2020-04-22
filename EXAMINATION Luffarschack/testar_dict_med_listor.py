import pandas as pd
import numpy as np
dict_med_listor = {
    'A' : [' ', ' ', ' '],
    'B' : [' ', ' ', ' '],
    'C' : [' ', ' ', ' ']
}
df = pd.DataFrame({'A': dict_med_listor['A'], 'B': dict_med_listor['B'], 'C':dict_med_listor['C']})
#ska jag ha en loop som skapar en ny dataframe varje varv vid input???
def inmatning():
    lista_att_markera = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))
    element_i_listan = str(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    """val = str.upper(input("Vad vill du göra med talen? Ange: +, -, *, %, eller / \n"))"""
    print(f"Du valde att placera markören på: {lista_att_markera}{element_i_listan} ")
    return lista_att_markera, element_i_listan

def placera_marker(dataframen, listan, elementet):
       
    
    return df2

#kanske kan köra med 1 lista och sätta A1 = spelplan[0]
#då kan man ha if-statement som säger att om elementet i listan ej är "-" så får man placera markör någon annanstans
#print(dict_med_listor['A'])
print(df)


#inmatning_lista, element_lista = inmatning()
#print(inmatning_lista, element_lista)
#print(dict_med_listor[inmatning_lista[0]])

#list_variabel = dict_med_listor[[inmatning_lista[0]]

#list_variabel[inmatning_lista[1]] = 'X'

#print(list_variabel)