# kanske hade man kunnat snygga till det på något sätt och återanvänt 
ett_tal = int(input("Ange ett tal: "))
def greater_than(ett_tal):
    great = (str(ett_tal) * ett_tal) 
    print("svar:", great)

def less_or_eq(ett_tal):
    for ett_tal in range(ett_tal+1):
        less = (str(ett_tal) * ett_tal)
        print("svar:", less)


if ett_tal > 5:
    greater_than(ett_tal)
elif ett_tal <= 5:
    less_or_eq(ett_tal)
