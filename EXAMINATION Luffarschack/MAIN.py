#kan använda den här för att skapa en "custom-size spelplan, behöver nog ändra i koden för rita_spelplan() dock"
spelplan = ['-' for x in range(10)]#tidigare skrev jag ut hela listan manuellt

#Global-test
#nuvarande_spelare = "X"

def rita_spelplan(): #Tom spelplan, går säkert att göra en loop för detta som kan ta ett argument
    print("  1   2   3")
    print("A",  spelplan[0] + " | " + spelplan[1] + " | " + spelplan[2])
    print("B",  spelplan[3] + " | " + spelplan[4] + " | " + spelplan[5])
    print("C",  spelplan[6] + " | " + spelplan[7] + " | " + spelplan[8])

#lägg in koden från meny_test här:
# man kan bara vinna när det är ens egen tur,

def byta_spelare(nuvarande_spelare):
    if nuvarande_spelare == "X":
        nuvarande_spelare = "O"
    elif nuvarande_spelare == "O":
        nuvarande_spelare = "X"
    return nuvarande_spelare
def placera_marker(nuvarande_spelare): #spelare
    
    koordinat = str.upper(input(f"Koordinat att placera markör {nuvarande_spelare} på:\n"))

    if koordinat[0] == "A" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = -1  
        position2 = position + int(koordinat[1])
        kontroll(nuvarande_spelare, position2)
      #borde kunna lägga till 3st if-satser som man vänder på för att tillåta format A1 och 1A  
    elif koordinat[0] == "B" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = 2
        position2 = position + int(koordinat[1])
        kontroll(nuvarande_spelare, position2)
    elif koordinat[0] == 'C' and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = 5  
        position2 = position + int(koordinat[1])
        kontroll(nuvarande_spelare, position2)
    # if spelplan[position2] == "-":
    #     spelplan[position2] = nuvarande_spelare
    # elif spelplan != "-":
    #     print("felaktig inmatning, försök igen")
    # rita_spelplan()

def kontroll(nuvarande_spelare, position2):
    if spelplan[position2] == "-":
        spelplan[position2] = nuvarande_spelare
    elif spelplan[position2] != "-":
        print("felaktig inmatning, försök igen")
    rita_spelplan()


def kolla_horisontell(): # kolla den sen för att lägga in felsäkerhet

    h_one_string = ""
    h_two_string = ""
    h_three_string = ""
    
    for x in spelplan[0:3]:
            h_one_string += x
    for x in spelplan[3:6]:
            h_two_string += x
    for x in spelplan[6:9]:
            h_three_string += x 
    if h_one_string == 'XXX' or h_one_string == 'OOO':       
       print(f"Spelet är slut, {h_one_string[0]} vann!") # ha en funktion somprint(f"Spelet är slut, {h_one_string[0]} vann!")ar detta?
                                                         #här avslutas spelet bara, den måste säga VEM som vann
    if h_two_string == 'XXX' or h_two_string == 'OOO':       
       print(f"Spelet är slut, {h_one_string[0]} vann!")
        
    if h_three_string == 'XXX' or h_three_string == 'OOO':       
       print(f"Spelet är slut, {h_one_string[0]} vann!")

def kolla_diagonal(): # kolla den sen för att lägga in felsäkerhet

    for x in spelplan[0:9]:
        if spelplan[0] == 'X' and spelplan[4] == 'X' and spelplan[8] == 'X':
            print(f"Diagonal vinst för X Vänster till Höger")
            break
        elif spelplan[0] == 'O' and spelplan[4] == 'O' and spelplan[8] == 'O':
            print(f"Diagonal vinst för O Vänster till Höger")
            break
        elif spelplan[2] == 'X' and spelplan[4] == 'X' and spelplan[6] == 'X':
            print(f"Diagonal vinst för X Höger till Vänster")
            break
        elif spelplan[2] == 'O' and spelplan[4] == 'O' and spelplan[6] == 'O':
            print(f"Diagonal vinst för O Höger till Vänster")
            break

# def start_spelare(): # låt denna sätta värdet på en global variabel "start_spelare", "nuvarande_spelare" kan sedan få ändra värdet på denna
#     spelare_1 = str.upper(input("Välj vem som ska starta spelet, X eller O: \n")) # kolla den sen för att lägga in felsäkerhet
#     spelare = []
#     if spelare_1 == "X": #göra spelarna till klasser eller kanske lista? så kan man spara info om de olika spelarna
#         spelare_2 = "O"
#     elif spelare_1 == "O":
#         spelare_2 = "X"
#     print(f"{spelare_1} börjar!")
#     spelare.append(spelare_1, spelare_2)
#     return spelare_1, spelare_2   
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

def kolla_vertikal():

    v_one_string = ""
    v_two_string = ""
    v_three_string = ""
    
    for x in spelplan[0:7:3]:
            v_one_string += x

    for x in spelplan[1:8:3]:
            v_two_string += x

    for x in spelplan[2:9:3]:
            v_three_string += x
        
    if v_one_string == 'XXX' or v_one_string == 'OOO':       
        print(f"Spelet är slut! {v_one_string[0]} vann med 3 i rad vertikalt i första kolumnen!!") # ha en funktion som printar detta?
    if v_two_string == 'XXX' or v_two_string == 'OOO':       
        print(f"Spelet är slut! {v_one_string[0]} vann med 3 i rad vertikalt i andra kolumnen!!")   
    if v_three_string == 'XXX' or v_three_string == 'OOO':       
        print(f"Spelet är slut! {v_one_string[0]} vann med 3 i rad vertikalt i tredje kolumnen!!")
# sätt vinnare till nuvarande_spelare (man kan vara vinna när det är ens egen tur)

def byta_spelare(nuvarande_spelare):
    if nuvarande_spelare == "X":
        nuvarande_spelare = "O"
    elif nuvarande_spelare == "O":
        nuvarande_spelare = "X"
    return nuvarande_spelare

# def skriva_ut_vinnare():
#      print("{nuvarande_spelare} vann!")

def kolla_om_spelet_spelas():
    kolla_efter_vinst()
    kolla_efter_oavgjort()

def kolla_efter_vinst():                #behöver en koll för om en marker redan är placerad där man försöker sätta ut
   kolla_horisontell()                  #behöver inmatningskontroll, något som ger ett felmeddelande men inte byter spelare och/eller avbryter spelet
   kolla_diagonal()
   kolla_vertikal()
   
   return
#kan även kallas/kolla 

#behöver lösa spelar_byte innan jag kan testa denna
def kolla_efter_oavgjort():
    for x in spelplan[0:9]: #denna kanske kan kolla efter om brädet är fullt, kolla mer på denna
        if x == "-":
            spelet_spelas = True       
    return

# def skapa_nuvarande_spelare():
#     nuvarande_spelare = start_spelare()
#     return nuvarande_spelare

def spela_spelet(): #försöka spara rund-antalet genom att lägga in en räknare
    spelet_spelas = True
    if spelet_spelas == True:
        runda = 0
        vinnare = None # den här eller spelet_spelas behöver ändras när någon vinner så att spelet tar slut
        rita_spelplan() 
        spelar_lista = start_spelare()
        nuvarande_spelare = spelar_lista[0]
        while spelet_spelas:
            placera_marker(nuvarande_spelare) #nuvarande_spelare
            kolla_om_spelet_spelas()
            nuvarande_spelare = byta_spelare(nuvarande_spelare)
            runda = runda+1
            print(f"Runda nr:{runda}")
    else:
        print("Spelet är slut")
    
    # if vinnare == 'X' or vinnare == 'O':
    #     print() 
    # elif vinnare == None:
    #     print("oavgjort")


spela_spelet()

#En omgång på ett 3x3 bräde har ett max-antal drag. det snabbaste man kan vinna på är efter 3(?) drag. kan ha en loop som körs i 3x3 antal "varv"? och när 
# "rundan" är 3 eller efter, först då kollar man efter vinnare

