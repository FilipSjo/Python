#x tar värde från listan, för varje varv hoppar den ett steg. % skriver ut vad som blivit över efter att vi delat talet; 3 % 2 ger 1, vilket tyder på att 3 är ett ojämnt tal
lista = [2,4,4,5,6,8,9,10,11]
for x in lista:
        if x % 2 ==0: 
            print(x, "Är ett jämnt tal")
        elif x % 2 !=0:
            print(x, "Är ett ojämnt tal, det får man inte")
            break