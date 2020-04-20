# denna funkar


def inmatning():
    try:
        tal1 = str(input("Ange ett alternativ i menyn \n"))
    except KeyError as error:
        print(f"{tal1} är inte ett giltigt värde, vänligen ange en siffra mellan 1-3")
    return tal1






def start1():
    print("Detta är start 1111")

def start2():
    print("Detta är start 2222")

def start3():
    print("Detta är start 3333")

def rita_meny(var1, meny):
    print(f"Du har valt meny-alternativ {var1} ")
    meny[var1]
#skapa en klass för meny istället
meny = {
    '1' : start1,
    '2' : start2,
    '3' : start3,
}
#meny[inmatning()]()
inmatning()
