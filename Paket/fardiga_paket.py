import pandas as pd
import numpy as np

lista = []
print("Ange 12 tal som kommer delas in i 3st listor")
while len(lista) <= 11:
    inmatning = int(input("Ange ett tal, \n"))
    lista.append(inmatning)
#stulen funktion för att dela en lista i angivet antal delar
#gillade den här lösningen bättre än att köra for-loop för input
def split_list(en_lista, antal_delar=1):
    length = len(en_lista)
    return [en_lista[i*length // antal_delar: (i+1)*length // antal_delar] 
             for i in range(antal_delar) ]




lista1, lista2, lista3 = split_list(lista, antal_delar=3)

lista4 = np.array(lista1)
lista5 = np.array(lista2)
lista6 = np.array(lista3)

df = pd.DataFrame({'Lista4':lista4, 'lista5':lista5, 'lista6':lista6})

print(f"Här kommer listorna ihopsatta till en Pandas DataFrame: \n {df}")


#eventuellt förbättra koden så att den lägger till Q1,Q2,Q3,Q4 som rubrik för varje element i arrayerna, vad fan som nu menas med det

