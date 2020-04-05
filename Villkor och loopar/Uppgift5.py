#skapar en tom lista som värdet ur "second_list" samt korresponderande index från "first_list" kan "appenderas" i efter varje varv. 
#printar även det lagrade värdet i "tupl" vid varje varv
first_list = [3,7,9,2,6]
second_list = [2,3,6,7,9]
lista = []
for i in second_list:
    tupl = (i, first_list.index(i))
    lista.append(tupl)
    print(tupl)
    
print(lista)









    

        