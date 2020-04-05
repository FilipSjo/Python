#!/usr/bin/env python
# coding: utf-8

# # Funktioner
# 
# ## Definitioner och användning
# 
# Ganska ofta behöver man använda samma kod flera gånger. Så här skulle det till exempel kunna se ut:

# In[40]:


print("Man kan räkna ut summan av 3 och 4 för att sedan skriva ut det på skärmen så här:")

term1 = 3
term2 = 4
sum = term1 + term2

print(f"\nSumman är {sum}\n")

print("Sedan kanske man har andra saker som händer, och långt senare vill man räkna ut en annan summa, så här:")

term1 = 4
term2 = 5
sum = term1 + term2

print(f"\nSumman är {sum}\n")

print("Det kan vara frestande att kopiera och klistra in, men tänk om något blir fel. Då måste man ändra på många ställen")
print("För nu räknar vi ut en ny summa:")

term1 = 5
term2 = 6
sum = term1 + term2

print(f"\nSumman är {sum}\n")

print("Loopar skulle kunna vara en lösning, men inte när det är kod mellan.")
print("Vi tar en summa till här, för att verkligen visa:")

term1 = 6
term2 = 7
sum = term1 + term2

print(f"\nSumman är {sum}\n")


# Vi kan använda funktioner. I det här fallet definierar vi funktionen så här:

# In[43]:


def print_sum(term1, term2):
    sum = term1 + term2
    print(f"\nSumman är {sum}\n")


# Programmet i exemplet ovan blir då:

# print("Man kan räkna ut summan av 3 och 4 för att sedan skriva ut det på skärmen så här:")
# 
# print_sum(3,4)
# 
# print("Sedan kanske man har andra saker som händer, och långt senare vill man räkna ut en annan summa, så här:")
# 
# print_sum(4,5)
# 
# print("Det kan vara frestande att kopiera och klistra in, men tänk om något blir fel. Då måste man ändra på många ställen")
# print("För nu räknar vi ut en ny summa:")
# 
# print_sum(5,6)
# 
# print("Loopar skulle kunna vara en lösning, men inte när det är kod mellan.")
# print("Vi tar en summa till här, för att verkligen visa:")
# 
# print_sum(6,7)

# Generellt ser funktionsdefinitioner ut något i den här stilen:

# In[47]:


def function_name(argument1, argument2 = 5):
    print(f"Argument 1: {argument1}\nArgument 2: {argument2}")
    return_value = argument1 - argument2
    return return_value


# Definitionen börjar med def följt av namn och argument
# 
# För att anropa en funktion skriver vi dess namn, med argumenten inom parentes efter. 

# In[50]:


print("Med argumenten 7 och 3: ")
function_name(7, 3)


# Vilket argument som är vilket beror på ordningen. Det går att ändra på genom att ange namnen som finns i funktionsdefinitionen. På det här viset:

# In[54]:


print("Med argumenten 8 och 2")
function_name(argument2=2, argument1=8)


# Tilldelningen i ett av argumenten innebär att det kommer att användas om inget annat anges

# In[51]:


print("\nMed bara argumentet 7:")
function_name(7)


# En funktion kan vid behov avslutas med nyckelordet return. Man säger då att den returnerar värdet efter return. För att en anropande funktion ska få tillgång till det värdet sätts en tilldelning till vänster om funktionsanropet:

# In[52]:


result = function_name(8, 1)

print(result)


# En funktion kan returnera flera värden genom att de separeras med komman:

# In[56]:


def multi_function(argument):
    return_value1 = argument + 1
    return_value2 = argument - 1
    return_value3 = argument + 2
    return return_value1, return_value2, return_value3


# Dessa kan tas emot av en annan kommaseparerad lista:

# In[59]:


return1, return2, return3 = multi_function(3)

print(return1)
print(return2)
print(return3)


# ...eller som en tupel

# In[58]:


returntuple = multi_function(3)

print(returntuple)


# De kan dock inte tas emot om den mottagande listan är för kort:

# In[60]:


return1, return2 = multi_function(3)

print(return1)
print(return2)


# ...eller för lång:

# In[62]:


return1, return2, return3, return4 = multi_function(3)

print(return1)
print(return2)
print(return3)
print(return4)


# ## Variablers räckvidd (scoping)
# 
# Variabler som tilldelas inne i en funktion är lokala om de inte först deklareras med nyckelordet global. Variabler som tilldelas utanför funktioner, i ett huvudprogram, är globala. Om det finns en lokal och en global variabel med samma nammn så används den globala. 
# 
# Om vi definierar en funktion som skriver till en lokal variabel (variable_1), en global variabel (variable_2), samt läser en variabel som inte definieras inne i funktionen (variabel_3):

# In[96]:


def local_variable_test():       

    variable_1 = "Lokal"
    
    global variable_2 
    variable_2 = "Lokal"
    
    print(f"I funktionen: \n"
          f"Variabel 1: {variable_1}, Variabel 2: {variable_2}, Variabel 3: {variable_3}\n\n")


# Och sedan kör funktionen med alla tre variablerna definierade globalt:

# In[97]:


variable_1 = "Global"
variable_2 = "Global"
variable_3 = "Global"
print(f"Före funktionen: \n"
      f"Variabel 1: {variable_1}, Variabel 2: {variable_2}, Variabel 3: {variable_3}\n\n")

local_variable_test()


print(f"Efter funktionen: \n"
      f"Variabel 1: {variable_1}, Variabel 2: {variable_2}, Variabel 3: {variable_3}")


# Så kan vi se följande:
# 
# 1. Variabel 1 definieras utan deklaration inne i funktionen. Det gör den till en lokal variabel. Eftersom lokala används före globala så kommer funktionen bara att påverka den lokala variabeln.
# 
# 2. Variabel 2 deklareras som global inne i variabeln. Det innebär att alla referenser till den kommer att gälla den globala variabeln. När funktionen skriver till den kommer den globala variabelns värde att skrivas över.
# 
# 3. Variabel 3 vare sig deklareras eller definieras inne i funktionen. Det finns alltså ingen lokal variabel 3, och tolken använder därför den globala variabeln. 

# In[100]:


c = 1
for a in range(3):
    b = a
    c += a
print(a)
print(b)
print(c)


# ## Docstrings
# 
# Docstrings används till att dokumentera en funktion så att den går att använda i help-funktionen.

# In[1]:


def testFunction():
    """Test the docstrings function

    If this function did anything more we would have written about it here.
    As it stands, there is not actually much to write about.
    But hopefully you note the blank line and the short description in the start."""

    pass #Needed because function cannot be empty


help(testFunction)


# ## Lambda-funktioner
# 
# Lambda-funktioner är funktioner som deklareras på en enda rad.

# In[10]:


plus = lambda var1, var2: var1 + var2
minus = lambda var1, var2: var1 - var2

def print_lambda(v1, v2, lambda_f):
    print(f"{v1} och {v2} ger: {lambda_f(v1, v2)}")

    

print_lambda(1, 3, plus)
print_lambda(3, 2, minus)
print_lambda(2.5, 2, lambda var1, var2: var1*var2)
print_lambda("hello ", "world", plus)


# ## Rekursion
# Rekursion är när funktioner anropar sig själva. I vissa lägen kan detta vara användbart. Det gäller dock att se till att ha ett slutvillkor på rekursionen.

# In[11]:


def factorial(n):
    print("Running factorial. n =", n)
    if(n < 0):
        ret_value = 0
    elif n <= 1:
        ret_value = 1
    else:
        ret_value = n*factorial(n-1)
    print("Returning value: ", ret_value)
    return ret_value


# In[12]:


print(factorial(1))
print(factorial(2))
print(factorial(3))


# In[ ]:




