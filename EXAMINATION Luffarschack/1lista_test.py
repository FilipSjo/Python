spelplan = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']        
def rita_spelplan():
    print("  A   B   C")
    print("1",  spelplan[0] + " | " + spelplan[1] + " | " + spelplan[2])
    print("2",  spelplan[3] + " | " + spelplan[4] + " | " + spelplan[5])
    print("3",  spelplan[6] + " | " + spelplan[7] + " | " + spelplan[8])
"""
dict_av_listor_med_koordinat = {
    'A' : [spelplan[0], spelplan[1], spelplan[2]],
    'B' : [spelplan[3], spelplan[4], spelplan[5]],
    'C' : [spelplan[6], spelplan[7], spelplan[8]]
}
"""
#ändra variabelnamn, skit i denna sålänge, använd 2 variabler från inmatning istället
"""def inmatning():
    lista_att_markera = str.upper(input("Ange koordinat att placera markör på  \nExempel: A1, B3, eller C2:  "))
    print(f"Du valde att placera markören på: {lista_att_markera} ")
    return lista_att_markera
"""
def inmatning():
    kolumn = str.upper(input("Kolumn att placera markör på  \nAnge A, B, eller C:  "))
    element = str(input("Rad att placera markör på \n\nAnge 0, 1, eller 2:  "))
    print(f"Du valde att placera markören på: {kolumn}{element} ")
    return kolumn, element

#loop som kollar igenom "lista att markera och för A, väljer lista A i dicten och sedan för 1 väljer element 0"
def placera_marker(kolumn, element, spelplan):
    for kolumn in spelplan:
        if kolumn == 'A':
            for element in kolumn:
                if element == '1':
                    spelplan[0] = 'X'
    return spelplan


rita_spelplan()
inmatning()
gris = placera_marker(inmatning(),spelplan)



