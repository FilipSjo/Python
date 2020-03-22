import datetime
now = datetime.datetime.now
var_name, var_age = str(input("Vad heter du?: ")), int(input("Hur gammal är du?: "))
print("Hej ", var_name, "\n" "Du blir 100 år gammal år:", 2020 + var_age ,"\n" "Du föddes år: ", 2020 - var_age)