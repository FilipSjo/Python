
ett_tal = int(input("Ange ett tal: "))
if ett_tal > 5:
    print("svar:", str(ett_tal) * ett_tal)
elif ett_tal <= 5:
    for ett_tal in range(ett_tal+1):
        print("svar:", str(ett_tal) * ett_tal)
