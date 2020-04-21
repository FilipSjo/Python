# denna funkar

#
def skriva_i_meny():
   
    tal1 = str(input("Ange ett alternativ i menyn \n"))
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

def rita_meny2(meny):
    print("Detta är menyn för spelet Luffarschack!:\n")
    print("1 för blablalba") 
    print("2 för blablalba")
    print("3 för blablalba")
    print("4 för blablalba")

meny = {
    '1' : start1,
    '2' : start2,
    '3' : start3,
}

rita_meny2(meny)
meny[skriva_i_meny()]()

