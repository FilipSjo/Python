
def start_spelare(): # låt denna sätta värdet på en global variabel "start_spelare", "nuvarande_spelare" kan sedan få ändra värdet på denna
    spelare_1 = str.upper(input("Välj vem som ska starta spelet, X eller O: \n")) # kolla den sen för att lägga in felsäkerhet
    spelare = []
    if spelare_1 == "X": #göra spelarna till klasser eller kanske lista? så kan man spara info om de olika spelarna
        spelare_2 = "O"
    elif spelare_1 == "O":
        spelare_2 = "X"
    print(f"{spelare_1} börjar!")
    spelare.append(spelare_1)
    spelare.append(spelare_2)
    return spelare

spelar_lista = start_spelare()

print(spelar_lista)