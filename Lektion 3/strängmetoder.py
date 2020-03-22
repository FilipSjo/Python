str0 = "Jag tYcker om äGg"
str1 = "inte"
str2 = "SPAM"
str3 = " "

#print(str0.lower())
#print(str0.capitalize())
#print(str0.upper())
#print(str0.swapcase())
str4, str5, str6 = str0.split(' ', 2)
str9, str10 = str6.split(' ', 1)
print(str9, str10)
#print(str0.rsplit())
#print(str0.title())
#print(str0.format())
#print(str4, str5, str1, str9.capitalize()
str7 = str4, str5, str1, str9
str12 = str3.join(str7)
#print(str7)
str13 = str4 + str3 + str5 + str3 + str1 + str3 + str9
print(str13)
str14 = str13.title()
print(str14.swapcase() + str3 + str2)