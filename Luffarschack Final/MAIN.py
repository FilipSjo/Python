import os.path # importerar denna för att kunna använda path.exists funktionen

spelplan = ['-' for tal in range(10)]


# # Globala variabler som nollställs efter varje spelomgång av en funktion, detta var en enklare lösning än att ha en massa returer
runda = 0
nuvarande_spelare = "" 
spelare1 = ""
spelare2 = ""
meny_val = ""
spelet_spelas = True

def kolla_om_filen_finns(filename): 
    return os.path.exists(filename)

                                # funktioner för att skriva till filer; som används som bas för statistiken
def skriva_statistik_till_X():
    with open ("X_rundor.txt", "a") as min_fil:
        rundan = str(runda)
        min_fil.writelines(f"{rundan}")
    
    skriva_statistik_rundor()

def skriva_statistik_till_O():
    with open ("O_rundor.txt", "a") as min_fil:
        rundan = str(runda)
        min_fil.writelines(f"{rundan}")
    
    skriva_statistik_rundor()

def skriva_statistik_till_oavgjorda():
    with open ("oavgjorda.txt", "a") as min_fil:
        min_fil.writelines("1")

    skriva_statistik_rundor()

def skriva_statistik_rundor():
    with open ("rundor.txt", "a") as min_fil:
        rundan = str(runda)
        min_fil.writelines(f"{rundan}")

def antal_oavgjorda():                      # konvertering och operationer på lista för att få en "naken"-sträng

    if kolla_om_filen_finns("oavgjorda.txt"): #os.path- grejen
        with open ("oavgjorda.txt", "r") as min_fil:   
            tecken = min_fil.readlines() #variabelnamn
            tecken = str(tecken)
            tecken = tecken.replace("'", "")
            tecken = tecken.replace("[", "")
            tecken = tecken.replace("]", "")
            antal_tecken = len(tecken)
        return antal_tecken

    return 0

def ta_fram_procent(antal_vinster_specifik_marker, totalt_antal_vinster):  # funktion för att beräkna procentsats
    if totalt_antal_vinster == 0:
        return 0
    else:
        procentsats = round((totalt_antal_vinster / antal_vinster_specifik_marker) * 100, 1)
        return procentsats

def antal_drag_per_match(): #hämtar från och lägger innehållet i en lista, konverterar till sträng och tar bort "list-delarna"
    if kolla_om_filen_finns("rundor.txt"):
        with open ("rundor.txt", "r") as min_fil:
            tecken = min_fil.readlines() #variabelnamn
            tecken = str(tecken)
            tecken = tecken.replace("'", "")
            tecken = tecken.replace("[", "")
            tecken = tecken.replace("]", "")
            antal_tecken = len(tecken)
            lista_med_drag = []
            for drag in tecken:
                drag = int(drag)
                lista_med_drag.append(drag)
            
            drag_per_match = (sum(lista_med_drag) / len(tecken))
    
            return drag_per_match, antal_tecken     

    return 0, 0

def antal_drag_X():             # hade nog kunna sätta ihop en funktion som tog hand om redundant kod här
    try:                        # denna hade nog funkat med enbart if-sats också, va lite nyfiken på hur den funkade dock
        with open ("X_rundor.txt", "r") as min_fil:
            tecken = min_fil.readlines() #variabelnamn
            tecken = str(tecken)
            tecken = tecken.replace("'", "")
            tecken = tecken.replace("[", "")
            tecken = tecken.replace("]", "")
            antal_tecken = len(tecken)
            lista_med_drag = []
            for drag in tecken:
                drag = int(drag)
                lista_med_drag.append(drag)
            
            drag_per_match = (sum(lista_med_drag) / len(tecken))
    
            return drag_per_match, antal_tecken     
    except IOError:
        return 0, 0

def antal_drag_O():

    if kolla_om_filen_finns("O_rundor.txt"):
        with open ("O_rundor.txt", "r") as min_fil:
            read = min_fil.readlines()
            reads = str(read)
            reads = reads.replace("'", "")
            reads = reads.replace("[", "")
            reads = reads.replace("]", "")
            reads2 = len(reads)
            listahehe = []
            for n in reads:
                n = int(n)
                listahehe.append(n)
            
            drag_per_match = (sum(listahehe) / len(reads))
            return drag_per_match, reads2
    
    return 0, 0

def printa_statistik():                             
    
    drag_per_match, totalt_spelade_matcher = antal_drag_per_match() 
    drag_for_O, antal_vunna_O = antal_drag_O()
    drag_for_X, antal_vunna_X = antal_drag_X()
    
    vunna_X_procent = ta_fram_procent(totalt_spelade_matcher, antal_vunna_X)
    vunna_O_procent = ta_fram_procent(totalt_spelade_matcher, antal_vunna_O)
    oavgjorda_matcher = antal_oavgjorda()
    oavgjorda_procent = ta_fram_procent(totalt_spelade_matcher, oavgjorda_matcher)

    print(f"Genomsnittligt antal drag per match: {drag_per_match}")
    print(f"Genomsnittligt antal drag till vinst för O: {drag_for_O}")
    print(f"Genomsnittligt antal drag till vinst för X: {drag_for_X}")
    print(f"Totalt antal spelade matcher: {totalt_spelade_matcher}")
    print(f"Antal vunna matcher för O: {antal_vunna_O}")
    print(f"Antal vunna matcher för X: {antal_vunna_X}")
    print(f"Antal oavgjorda matcher: {oavgjorda_matcher} ")
    print(f"Vinstprocent för X: {vunna_X_procent} %")
    print(f"Vinstprocent för O: {vunna_O_procent} %")
    print(f"Procentuell andel matcher som är oavgjorda {oavgjorda_procent} %")
    skriva_i_meny()

def rita_meny():
    print("Detta är menyn för spelet Luffarschack!:\n")
    print("ange 1 för att visa statistik") 
    print("ange 2 för att spela")
    print("ange 3 för att avsluta")

def skriva_i_meny():
    global meny_val
    rita_meny()
    tal1 = str(input("Ange ett alternativ i menyn \n"))  # if-satsen som gör att vi bara tar emot rätt input
    if tal1 == "1" or tal1 == "2" or tal1 == "3":
        meny_val = tal1
        meny[meny_val]()
    else:
        print("Ogiltigt menyval.")
        skriva_i_meny()

def spela_igen(): # fixa så att inputen blir rätt
 
    ja_nej = str.upper(input("Spela igen? Y / N \n"))
    if ja_nej == "Y": 
        nolla_variabler(spelplan)
        spela_spelet()
    elif ja_nej == "N":
        print("Åter till menyn.") # måste fixa så att den avslutar här
        skriva_i_meny()        
    elif ja_nej != "Y" or "N":
        print("Ogiltigt alternativ.")
        spela_igen()
        

def nolla_variabler(spelplanen):
    global runda
    global nuvarande_spelare
    global meny_val
    global spelplan
    global spelare1
    global spelare2

    runda = 0
    nuvarande_spelare = ""
    spelare1 = ""
    spelare2 = ""
    meny_val = ""
    spelplan = ['-' for tal in range(10)]


def rita_spelplan(): #Tom spelplan, går säkert att göra en loop för detta som kan ta ett argument
    print("  1   2   3")
    print("A",  spelplan[0] + " | " + spelplan[1] + " | " + spelplan[2])
    print("B",  spelplan[3] + " | " + spelplan[4] + " | " + spelplan[5])
    print("C",  spelplan[6] + " | " + spelplan[7] + " | " + spelplan[8])


def kollaOmTrue(character, number): # kör kontroll av input i placera_marker(): 
    if character:                   
        if number:
            return False
    return True

def placera_marker(): #spelare try, catch skit här  #tar bort nuvarande_spelare då den är global
    #jag får göra en del av kontrollen här, dvs INPUT-delen! range + tecken (format)
   #kanske kan lägga in en while-loop med try-catch grej här vid inputen
    global spelare1
    global spelare2
    input_bokstav = False
    input_siffra = False
   
    while kollaOmTrue(input_bokstav, input_siffra):  #Är false från början och loopen körs sålänge inte båda är TRUE
        
        korrekt_input = 'A', 'B', 'C'

        koordinat = str.upper(input(f"Koordinat att placera markör {nuvarande_spelare} på:\n"))
        
        antal_tecken = len(koordinat) 
        
        if antal_tecken == 2: # här kontrollerar vi "längden" på input så att den matchar
            if any(bokstav in koordinat[0] for bokstav in korrekt_input): # om bokstav i koordinat[0] finns med i korrekt_input går vi vidare
                input_bokstav = True

            if any(siffra in koordinat[1] for siffra in ('1', '2', '3')):
                input_siffra = True

        if kollaOmTrue(input_bokstav, input_siffra): # båda påstående måste vara sanna för att vi ska få ta dom vidare till kontroll()- funktionen
            print("Ange giltig koordinat !")
            rita_spelplan()


    if koordinat[0] == "A" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'): # matchar första bokstaven
        position = -1  # beskriv detta med kommentarer
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) 
        
    elif koordinat[0] == "B" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'): # lägg till omvänt statement för om man skriver siffra först
        position = 2
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) 
        
    elif koordinat[0] == "C" and (koordinat[1] == '1' or koordinat[1] == '2' or koordinat[1] == '3'):
        position = 5  
        position2 = position + int(koordinat[1])
        kontroll(position2, spelare1, spelare2) 
        
                                        
def kontroll(position2, spelaren1, spelaren2): # kontrollerar om koordinaten / platsen där man försöker sätta marker redan är tagen
    global runda
    global nuvarande_spelare
    global spelare1
    global spelare2
    if spelplan[position2] == "-":
        spelplan[position2] = nuvarande_spelare
        rita_spelplan()
        
    elif spelplan[position2] == ("X" or "O"):
        runda = runda-1 #räknar upp runda för varje varv, tar den dock - här ifall man matar in fel så att runda inte blir fel i slutet
        nuvarande_spelare = byta_spelare(spelare1, spelare2) 
        rita_spelplan()
        print("Marker redan placerad på angiven plats, försök igen")
    elif spelplan[position2] == ("O" or "X"): 
        runda = runda-1 
        nuvarande_spelare = byta_spelare(spelare1, spelare2) # byter spelare för varje varv (markör)
        rita_spelplan()
        print("Marker redan placerad på angiven plats, försök igen")   


def kolla_horisontell(): # kontrollerar vinstkriterier för horisontella rader

    horisontell_rad_1 = "" 
    horisontell_rad_2 = ""
    horisontell_rad_3 = ""
    for tecken in spelplan[0:3]:
            horisontell_rad_1 += tecken                               
    if horisontell_rad_1 == 'XXX' or horisontell_rad_1 == 'OOO':       
        return horisontell_rad_1[0]  
    for tecken in spelplan[3:6]:
            horisontell_rad_2 += tecken
    if horisontell_rad_2 == 'XXX' or horisontell_rad_2 == 'OOO':       
        return horisontell_rad_2[0]
    for tecken in spelplan[6:9]:
            horisontell_rad_3 += tecken 
    if horisontell_rad_3 == 'XXX' or horisontell_rad_3 == 'OOO':       
        return horisontell_rad_3[0]       
    else:
        return None  

def kolla_diagonal(): 
    for tecken in spelplan[0:9]:  #variabelnamn
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
                     
    else:
        print("Ogiltigt val.")
        rita_spelplan()
        start_spelare()
        
def avsluta(): # fixa denna så att den stänger ner programmet
    global spelet_spelas
    spelet_spelas = False
    
def kolla_vertikal():
    vertikal_rad1 = "" #variabelnamn
    vertikal_rad2 = ""
    vertikal_rad3 = ""
    for tecken in spelplan[0:7:3]:
            vertikal_rad1 += tecken
    for tecken in spelplan[1:8:3]:
            vertikal_rad2 += tecken
    for tecken in spelplan[2:9:3]:
            vertikal_rad3 += tecken
        
    if vertikal_rad1 == 'XXX' or vertikal_rad1 == 'OOO':       
        return vertikal_rad1[0]
           
    if vertikal_rad2 == 'XXX' or vertikal_rad2 == 'OOO':       
        return vertikal_rad2[0]
        
    if vertikal_rad3 == 'XXX' or vertikal_rad3 == 'OOO':       
        return vertikal_rad3[0]    
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
    nolla_variabler(spelplan)
    start_spelare()
    rita_spelplan()   
    nuvarande_spelare = spelare1
    while spelet_spelas == True:                     # huvudloop, tror inte 
        placera_marker() 
        vinnare = kolla_efter_vinst()
        nuvarande_spelare = byta_spelare(spelare1, spelare2) 
        runda = runda+1 
        print(f"Runda nr:{runda}")
        if runda >= 9:
            print("Spelet är över, oavgjort")
        
            skriva_statistik_till_oavgjorda()
            spela_igen()
        elif vinnare != None and runda < 9:
            if vinnare == "O":
                print(f"{vinnare} vann!\nSpelet är över!")
              
                skriva_statistik_till_O()
               
            elif vinnare == "X":
                print(f"{vinnare} vann!\nSpelet är över!")
             
                skriva_statistik_till_X()
           
            spela_igen()

meny = {
    '1' : printa_statistik,
    '2' : spela_spelet,
    '3' : avsluta,
}

skriva_i_meny()


