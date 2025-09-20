x = input("Enter int x :")
y = input("Enter int y :")

# input() function only takes string input

print(f"FYI - x+y - {x+y} returns the concatenation so use int(x)+int(y) - {int(x)+int(y)}")

x = input("Enter float x :")
y = input("Enter float y :")

print(f"FYI - x+y - {x+y} returns the concatenation so use float(x)+float(y) - {float(x)+float(y)}")
# round() parameters -> (number[, ndigits])
print(f"round(float(x)+float(y)) - {round(float(x)+float(y))} , rounding to 2 decimal units round(float(x)+float(y),2) - {round(float(x)+float(y),2)}")


# In a formatted string use {{ }} to denote {}
print(f"To print numbers in US style(1,000,000 etc) use f\"{{number:,}}\"")
print(f"{1000:,}")

print(f"To print decimals rounded to n digits(9.67 - rounded to 2  etc) use f\"{{number:.2f}}\"")
print(f"9.66678 is printed as {9.66678:.2f} on using f\"{{number:.2f}}\"")