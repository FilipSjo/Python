import pandas as pd
import numpy as np

lista1 = ['','','']
lista2 = ['','','']
lista3 = ['','','']
lista4 = np.arange(1, 4)
lista5 = np.arange(4, 7)
lista6 = np.arange(7, 10)
lista7 = ['1','2','3']
lista8 = ['4','5','6']
lista9 = ['7','8','9']

lista10 = []
#eventuellt att printen konverterar från siffror till '' vid print för att det ska vara tydligare att se spelplanen
df = pd.DataFrame({'A':lista7, 'B': lista8, 'C': lista9})
df2 = pd.DataFrame({'A':lista1, 'B': lista2, 'C': lista3})
#räkna varv i loopen så att man kan se vilket "Drag-nummer" man är på, detta kan vara bra för statistikdelen
"""print("Ange 12 tal som kommer delas in i 3st listor")
while len(lista) <= 11:
    inmatning = int(input("Ange ett tal, \n"))
    lista.append(inmatning)
#gillade den här lösningen bättre än att köra for-loop för input
def split_list(en_lista, antal_delar=1):
    length = len(en_lista)
    return [en_lista[i*length // antal_delar: (i+1)*length // antal_delar] 
             for i in range(antal_delar) ]
"""
# Indexering: https://brohrer.github.io/dataframe_indexing.html
#.set_index('name', inplace=True)
"""
for i in df:
    replace
"""

#kör en strängcheck, dels för att kolla om det går att sätta in siffran
"""for i in range(len(data)): #kanske kan vara något för att kolla igenom om element är "länkade"
    if data["Type"][i] == "Grass": 
        Type_new[i]="Green"
"""
#print(f"Aktuell spelplan efter drag: \n {df}")
#cpds = df.loc[1, 'B']
#hej = df.replace({'A' : 1}, 'X')
#print(hej)
#df2.set_index('name', inplace=True)
#hej2 = df2.replace({'A' : }, 'X')

#funktion för detta som tar 2 argument, sedan en annan funktion som gör samma sak fast ersätter med 'O'
hej = df.replace(['A','1'], 'X') #kolla här om det bara behövde vara '1', eller 1

print(hej)

#för att snygga till kanske man ska ha elementen i lista i form av en dict så att brädet ser tomt ut i början,
#för att sedan köra en "swap" och replace innan man printar ut