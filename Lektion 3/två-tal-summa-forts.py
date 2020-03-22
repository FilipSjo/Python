var_a, var_b = float(input("tal 1: ")), float(input("tal 2: "))
#print("Talen är:  %d och %d med %-formatering" %(var_a, var_b))
#print("Talen är: {} och {} med str.format".format(var_a, var_b))
print(f"talen är med f-strings: {var_a} och {var_b}")
print("differensen av talen är: ", var_a - var_b, "\n", "produkten av talen är: ", 
var_a * var_b, "\n", "kvoten av talen är: ", var_a / var_b)