from math import sqrt
print("Räkna ut hypotenusan på en rätsidig triangel")
kat_a, kat_b = float(input("Skriv in längden på katet A: ")), float(input("Skriv in längden på katet B: "))
print("En triangel med katetlängd: ", kat_a, "och katetlängd: ", kat_b, "Har en längd på hypotenusan av: ", sqrt(kat_a**2 + kat_b**2))