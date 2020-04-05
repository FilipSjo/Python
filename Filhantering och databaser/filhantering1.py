#Övningar från web: 1-7, 16 & 17
#8-13 är valfria
#SQL-övningar: 1,6,7
#9-16 valfria

#var uppmärksam på sökvägen, funkar nu för att programfilen och filen som ska läsas in ligger i samma mapp

#kan vara nödvändigt att stänga filen för att den ska kunna läsas in
#den gillar inte å,ä,ö
#läser hela filen
# 111111111111111111111111111111111
"""with open("testfil.txt", "rt") as min_fil:
    print(min_fil.read())
"""


#"snodd kod", dvs den del som loopar smart. Den printar dock ut antal rader angivna i range()
# 222222222222222222222222222222
"""with open("testfil.txt", "rt") as min_fil:
    
    rader = [next(min_fil) for line in range(2)]
    print(rader)
"""
#appendar text till en fil och skriver ut det som vi ville lägga till
# 333333333333333333333333333333333
"""def text_to_string():
    string = str(input("Type what you want added to the file: \n"))
    return string

def add_to_file(to_be_added):
    with open("testfil.txt", "a") as min_fil:
        min_fil.write(to_be_added)
    return to_be_added

#text_to_string()
added_text = add_to_file(text_to_string())
print(added_text)
"""
#splitlines delar en sträng, eller det här fallet "dokumentet" baserat på när det kommer en radbrytning, 
#kolla mer på denna!
# 4444444444444444444444444444444444
"""with open("testfil.txt", "rt") as min_fil:
    
    rader = min_fil.read().splitlines()
    sista_raden = rader[-1]
    print(sista_raden)
"""
# 555555555555555555555
# Write a Python program to read a file line by line and store it into a list

#loopa igenom filen, spara rad för rad som appends? i en lista

# for-loopen fixar problemet men det ser kanske inte jättesnyggt ut , testar en annan lösning
"""with open("testfil.txt", "rt") as min_fil:
    lista = []
    
    for line in min_fil:
        lista.append(line)
print(lista)"""
#samma sak fast med funktionen "readlines", mindre kod?
"""with open("testfil.txt", "rt") as min_fil:
    lista = min_fil.readlines()
    print(lista)"""
#6666666666666666666
# genom att ändra från "readlines" till "read-funktionen" så skapas en variabel (sträng) istället för en lista 
"""with open("testfil.txt", "rt") as min_fil:
    variabel = min_fil.read()
    print(variabel)
"""
#777777
"samma kod som för uppgift 5"

#16
#".closed kollar status på filen, resten sköts av en enkel if-sats"
#det kanske finns något sätt att hantera felmeddelanden?
"""min_fil = open("testfil.txt", "rt")

if min_fil.closed:
    print("Hej jag är stängd")
else:
    print("hej jag var öppen, men stängdes korrekt?!")

min_fil.close()"""
#17
#använder .replace(), för att ersätta escape-tecknen 
#detta är dock gjort här UTAN funktion
"""with open("testfil.txt", "rt") as min_fil:
    
    replace_newline = min_fil.read().replace('\n', '')
    print(replace_newline)"""
#rstrip är tydligen en metod som kan göra exakt det fast lite enklare,
#tycker att detta borde ha fungerat
"""with open("testfil.txt", "rt") as min_fil:
    for line in min_fil:
        line.rstrip('\n')
    print(min_fil.readlines())
"""
def newline(file_name):
    flist = open(file_name).readlines()
    return [line.rstrip('\n') for line in flist]

print(newline("testfil.txt"))