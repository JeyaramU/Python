# while loop
# Ctrl+C cancels an infinite loop in the terminal

i = 3

# String can be printed in iteration inside the print method
# \n is needed as this print 
print(" print( test\\n * number_of_times , end=\"\")")
print("Printing without loops and single print function with next line escape sequence\n" * 3, end = "")

while i !=0:
    print(f"Printing {i}")
    # i -1 == i -= 1  ; i-- does not work in python
    i = i-1 

# for loop

for i in [3, 2, 1]:
    print(f"Printing {i}")
    i = i-1

print("Using for i in range(3) will assume i as 0 and starts it, not the global variable in code(in code i = 3)")
for i in range(3):
    print(f"Printing {i}")
