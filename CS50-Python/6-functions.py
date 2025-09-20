# def = define

name = input("Enter name : ")

# name in 3rd line can also be used directly in 10th line without passing as parameter as name is a global variable without a main() function 
def hello(to):
    """
    Everything that is indented after : will be treated as function
    """
    print(f"Hello {to}")

def helloWithDefault(name = "World"):
    print(f"Hello {name}")

# The function call needs to be kept only below the def, Python's interpretor expects it by default
# To overcome this we need the function call in main function, As the main function executes its contents only at call
# Then call main only at the end of all def as python goes line by line 
hello(name)
helloWithDefault()
helloWithDefault(name)

# Example of main functiom
def main():
    # int conversion directly on input
    x = int(input("Enter x for square : "))
    print(f" {x} squared is {square(x)}")

# Call to main() will not work here as the interpretor does not know whats square(x)
# main()

def square(n):
    # pow(n,2) does the same functionality as n * n and n ** 2 (a ** b is a power b)
    return pow(n,2)

main()