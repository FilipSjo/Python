# gjorde 2st variabler för att det ska vara enklare att byta det hårdkodade värdet
#sålänge gissat_tal2 inte är samma som gissat_tal så körs loopen
gissat_tal = 100
gissat_tal2 = 0
while gissat_tal2 != gissat_tal:
    gissat_tal2 = int(input("Gissa vilket heltal jag tänker på: "))
    if gissat_tal2 < gissat_tal: 
        print("Fel, för LÅGT! Försök igen")
        
    elif gissat_tal2 > gissat_tal:
        print("Fel, för HÖGT! Försök igen")
        
    elif gissat_tal2 == gissat_tal:
        print("Rätt!")
        
      

            