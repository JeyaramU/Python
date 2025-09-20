# We can use infinite loop to get a valid input from the user

while True:
    n = int(input("Enter a number :"))
    if n < 0:
        print("Only positive integers are allowed")
        continue
    else:
        # If the input is needed and the infinite loop is inside a function, you can also use retutn n instead of break
        break