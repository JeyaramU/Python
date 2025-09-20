# if conditions with logical operators

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")

if x > 0 and y > 0:
    print("Both x and y are positive")

elif x > 0 or y > 0:
    print("At least one of x or y is positive")

# % can be used to check parity, remainder after divinding
def evenCheck(num):
    # The if can be removed by returning directly like -> return n % 2 == 0
    if n % 2 == 0:
        return True
    else:
        return False # F and T should be in caps

print("To check if a number is even or odd using %")
n = int(input("Enter the number(int) : "))
if evenCheck(n):
    print("Its an even number - minus is not considered ")
else:
    print("Its an odd number - minus is not considered ")



