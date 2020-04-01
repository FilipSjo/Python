first_list = [3,7,9,2,6]
second_list = [2,3,6,7,9]
lista = []
for i in second_list:
    tupl = (i, first_list.index(i))
    lista.append(tupl)
    print(tupl)
    
print(lista)









    

        