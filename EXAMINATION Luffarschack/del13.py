import pandas as pd
import numpy as np


df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})
#köra en int-konvertering? Behövdes inte
print(df)

def replace_for_x(str_1, int_1):
    hej2 = df.replace({str_1:{int_1:'X'}})
    #hej2 = df.replace([str_3, str_4], 'X')
    return hej2
print(replace_for_x('A', 3))
#hej = df.replace({'A':{1:'X'}})

print(replace_for_x('A', 3))

#om man skapar listor , bör man kunna använda [i]-grejen för att hitta rätt: dvs index -2 i lista A, osv,
#då kanske listan kan vara tom
#fixa i så fall så att man kan skriva '3a', 'a3' dvs ej caps-känsligt
#loop som uppdaterar valfri lista med antingen 'O' eller 'X'
#kollar om värdet som ska ersättas redan är 'O' eller 'X', i så fall ge felmeddelande
#kollar igenom listorna efter "win-conditions"
#sparar listorna i en dataframe som skrivs ut varje runda, på så sätt man kan se gamla drag osv(sparas som variabel)
