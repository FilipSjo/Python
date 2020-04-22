#kan använda den här för att skapa en "custom-size spelplan, behöver nog ändra i koden för rita_spelplan() dock"
spelplan = ['-' for x in range(10)]

#Global-test
runda = 0
#definerar den här globalt för att kunna hämta in den i funktionerna på ett enklare sätt
nuvarande_spelare = "" #X
#spelar_lista = ["",""]
spelare1 = ""
spelare2 = ""
meny_val = ""
def rita_meny():
    print("Detta är menyn för spelet Luffarschack!:\n")
    print("ange 1 för att välja vilken markör som ska börja") #ändra till visa statistik eller dylikt (lägg till att man kan nolla statistiken)
    print("ange 2 för att spela")
    print("ange 3 för att avsluta")

def skriva_i_meny():
    global meny_val
    rita_meny()
    tal1 = str(input("Ange ett alternativ i menyn \n"))
    if tal1 == "1" or tal1 == "2" or tal1 == "3":
        meny_val = tal1
        #return tal1
    else:
        print("Ogiltigt alternativ.")
        skriva_i_meny()

def spela_igen():

    ja_nej = str.upper(input("Spela igen? Y / N \n"))
    if ja_nej == "Y": 
        nolla_variabler(spelplan)
        #rita_spelplan() kanske inte behövs
        spela_spelet()
    else:
        print("Avslutar.") # måste fixa så att den avslutar här

def nolla_variabler(spelplanen):
    global runda
    global nuvarande_spelare
    #global spelar_lista
    global meny_val
    global spelplan
    global spelare1
    global spelare2

    runda = 0
    nuvarande_spelare = ""
    spelare1 = ""
    spelare2 = ""
    meny_val = ""
    spelplan = ['-' for x in range(10)]


def rita_spelplan(): #Tom spelplan, går säkert att göra en loop för detta som kan ta ett argument
    print("  1   2   3")
    print("A",  spelplan[0] + " | " + spelplan[1] + " | " + spelplan[2])
    print("B",  spelplan[3] + " | " + spelplan[4] + " | " + spelplan[5])
    print("C",  spelplan[6] + " | " + spelplan[7] + " | " + spelplan[8])

def placera_marker(): #spelare try, catch skit här  #tar bort nuvarande_spelare då den är global
    #jag får göra en del av kontrollen här, dvs INPUT-delen! range + tecken (format)
   #kanske kan lägga in en while-loop med try-catch grej här vid inputen
    global spelare1
    global spelare2
    
    while True:

        koordinat = str.upper(input(f"Koordinat att placera markör {nuvarande_spelare} på:\n"))
    
        if any([koordinat[0] == 'A', koordinat[0] == 'B', koordinat[0] == 'C', koordinat[1] == '1', koordinat[0] == '2', koordinat[0] == '3']):
            break
           
#if (koordinat[0] == "A" or koordinat[0] == "B" or koordinat[0] == "C") and (koordinat[1] == "1" or koordinat[1] == "2" or koordinat[1] == "3"):# kolla denna sen!!
    
    if koordinat[0] == "A" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = -1  # beskriv detta med kommentarer
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) #hade koordinat här förut också, hade spelar_lista
        #borde kunna lägga till 3st if-satser som man vänder på för att tillåta format A1 och 1A  
        #return position2
    elif koordinat[0] == "B" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'): # lägg till omvänt statement för om man skriver siffra först
        position = 2
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) # KOLLA KONTROLL hade spelar_lista
        #return position2
    elif koordinat[0] == "C" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = 5  
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) # KOLLA KONTROLL #kolla nuvarande_spelare, den är global hade spelar_lista
        
                                        
def kontroll(position2, spelaren1, spelaren2): #vet inte om den här är nödvändig, KOLLA DENNNA NUVARANDE_spelare borta, global
    global runda
    global nuvarande_spelare
    global spelare1
    global spelare2
    if spelplan[position2] == "-":
        spelplan[position2] = nuvarande_spelare
        rita_spelplan()
        #ha en return här som tillåter loopen att gå till nästa steg?
    elif spelplan[position2] == ("X" or "O"): # testa denna
        runda = runda-1 # kanske flyttar den här i while-loopen
        nuvarande_spelare = byta_spelare(spelare1, spelare2) #  tog bort nuvarande_spelare den är global
        rita_spelplan()
        print("felaktig inmatning, försök igen PLATSEN ÄR BEBODD")
    elif spelplan[position2] == ("O" or "X"): # testa denna
        runda = runda-1 # kanske flyttar den här i while-loopen
        nuvarande_spelare = byta_spelare(spelare1, spelare2) #  tog bort nuvarande_spelare den är global
        rita_spelplan()
        print("felaktig inmatning, försök igen PLATSEN ÄR BEBODD")   


def kolla_horisontell(): # kolla den sen för att lägga in felsäkerhet

    h_one_string = ""
    h_two_string = ""
    h_three_string = ""
    for x in spelplan[0:3]:
            h_one_string += x                               # tog bort spelet_spelas = False i varje if-sats
    if h_one_string == 'XXX' or h_one_string == 'OOO':       
        return h_one_string[0]  
    for x in spelplan[3:6]:
            h_two_string += x
    if h_two_string == 'XXX' or h_two_string == 'OOO':       
        return h_two_string[0]
    for x in spelplan[6:9]:
            h_three_string += x 
    if h_three_string == 'XXX' or h_three_string == 'OOO':       
        return h_three_string[0]       
    else:
        return None  

def kolla_diagonal(): 
    for x in spelplan[0:9]: 
        if spelplan[0] == 'X' and spelplan[4] == 'X' and spelplan[8] == 'X':
            return spelplan[0]
        elif spelplan[0] == 'O' and spelplan[4] == 'O' and spelplan[8] == 'O':      
            return spelplan[0]
        elif spelplan[2] == 'X' and spelplan[4] == 'X' and spelplan[6] == 'X':
            return spelplan[2]
        elif spelplan[2] == 'O' and spelplan[4] == 'O' and spelplan[6] == 'O':
            return spelplan[2]
        else:    
            return None
def start_spelare(): 
    global spelare1
    global spelare2
    
    spelare1 = str.upper(input("Välj vem som ska starta spelet, X eller O: \n")) # kolla den sen för att lägga in felsäkerhet

    if spelare1 == "X" or spelare1 == "O":
        if spelare1 == "X": 
            spelare2 = "O"
        elif spelare1 == "O":
            spelare2 = "X"
        print(f"{spelare1} börjar!")
        # spelar_lista[0] = spelare1s_marker #tidigare append
        # spelar_lista[1] = spelare2s_marker  # dessa variabelnamn suger, fixa detta sen
                     
    else:
        print("Ogiltigt alternativ.")
        rita_spelplan()
        start_spelare()
        
        #start_spelare()
    # spelare.append(spelare1s_marker)
    # spelare.append(spelare2s_marker)  # dessa variabelnamn suger, fixa detta sen
    # return spelare

def avsluta(): # fixa denna så att den stänger ner programmet
    return

def kolla_vertikal():
    v_one_string = "" #variabelnamn
    v_two_string = ""
    v_three_string = ""
    for x in spelplan[0:7:3]:
            v_one_string += x
    for x in spelplan[1:8:3]:
            v_two_string += x
    for x in spelplan[2:9:3]:
            v_three_string += x
        
    if v_one_string == 'XXX' or v_one_string == 'OOO':       
        return v_one_string[0]
           
    if v_two_string == 'XXX' or v_two_string == 'OOO':       
        return v_two_string[0]
        
    if v_three_string == 'XXX' or v_three_string == 'OOO':       
        return v_three_string[0]    
    else:
        return None

def byta_spelare(spelaren1, spelaren2): # tog bort nuvarande_spelare, lägg tillbaka om icke-global
    global runda
    global nuvarande_spelare
    global spelare1
    global spelare2
    if nuvarande_spelare == spelare1: #ändrar dessa från X och O till spelar_lista[1] och [0]
        nuvarande_spelare = spelare2
    elif nuvarande_spelare == spelare2:
        nuvarande_spelare = spelare1
    return nuvarande_spelare

def kolla_efter_vinst():                
    horisontell = kolla_horisontell()                  
    diagonal = kolla_diagonal()
    vertikal = kolla_vertikal() # la kolla den här metoden
   
    if horisontell != None:
        vinnare = horisontell
        return horisontell
        
    elif diagonal:
        vinnare = diagonal
        return diagonal
    
    elif vertikal:
        vinnare = vertikal
        return vertikal
    else:
        return None 
     
def spela_spelet(): 
    global runda
    global nuvarande_spelare
    global spelare1
    #spelet_spelas = True
    # kanske behöver vara global för att få räknaren att fungera
    rita_spelplan() 
    start_spelare()   # om jag bryter ut denna funktion och lägger den i menyn så kan man sätta värde
    nuvarande_spelare = spelare1
    while True: 
        placera_marker() 
        vinnare = kolla_efter_vinst()
        nuvarande_spelare = byta_spelare(spelare1, spelare2) 
        runda = runda+1 
        print(f"Runda nr:{runda}")
        if runda >= 9:
            print("Spelet är över, oavgjort")
            spela_igen()
        elif vinnare != None and runda < 9:
            print(f"{vinnare} vann!\nSpelet är över!")
            #skriva skit till fil här kanske? 
            spela_igen() # bör kanske vara spelet_spelas = False
    return

meny = {
    '1' : start_spelare,
    '2' : spela_spelet,
    '3' : avsluta,
}

skriva_i_meny()
meny[meny_val]()



#def statistik_funktion():
    #skriver runda
