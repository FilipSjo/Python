var_min = int(input("Skriv in antal minuter: "))
print(var_min, "minuter motsvarar: ",var_min // 60 ,"timmar och", var_min%60, "minuter")
#       heltalsdivisionen här ovan verkar spara divisionsresten så att vi kan använda den direkt, fattar inte riktigt hur det funkar men det gör det