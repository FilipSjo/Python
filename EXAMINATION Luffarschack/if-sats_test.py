#spelplan = ['-' for x in range(10)]

spelplan = ['-', '-', '-',
            '-', '-', '-',
            '-', '-', '-']   

def kolla_horisontell():

    h_one_string = ""
    h_two_string = ""
    h_three_string = ""
    
    for x in spelplan[0:3]:
            h_one_string += x

    for x in spelplan[3:6]:
            h_two_string += x

    for x in spelplan[6:9]:
            h_three_string += x
        
    if h_one_string == 'XXX' or h_one_string == 'OOO':       
        print("Spelet är slut!") # ha en funktion som printar detta?
                                    #här avslutas spelet bara, den måste säga VEM som vann
    if h_two_string == 'XXX' or h_two_string == 'OOO':       
        print("Spelet är slut!")
        
    if h_three_string == 'XXX' or h_three_string == 'OOO':       
        print("Spelet är slut!")

def kolla_diagonal(): 

    for x in spelplan[0:9]:
        if spelplan[0] == 'X' and spelplan[4] == 'X' and spelplan[8] == 'X':
            print(f"Diagonal vinst för X Vänster till Höger")
            break
        elif spelplan[0] == 'O' and spelplan[4] == 'O' and spelplan[8] == 'O':
            print(f"Diagonal vinst för O Vänster till Höger")
            break
        elif spelplan[2] == 'X' and spelplan[4] == 'X' and spelplan[6] == 'X':
            print(f"Diagonal vinst för X Höger till Vänster")
            break
        elif spelplan[2] == 'O' and spelplan[4] == 'O' and spelplan[6] == 'O':
            print(f"Diagonal vinst för O Höger till Vänster")
            break

def kolla_vertikal():

    v_one_string = ""
    v_two_string = ""
    v_three_string = ""
    
    for x in spelplan[0:7:3]:
            v_one_string += x

    for x in spelplan[1:8:3]:
            v_two_string += x

    for x in spelplan[2:9:3]:
            v_three_string += x
        
    if v_one_string == 'XXX' or v_one_string == 'OOO':       
        print("Spelet är slut!") # ha en funktion som printar detta?
    if v_two_string == 'XXX' or v_two_string == 'OOO':       
        print("Spelet är slut!")   
    if v_three_string == 'XXX' or v_three_string == 'OOO':       
        print("Spelet är slut!")


kolla_diagonal()

kolla_horisontell()

kolla_vertikal()
