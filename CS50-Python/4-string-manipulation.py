name = input("Enter name : ")

print("Manipulations done")

print(f"Entered Name - {name}")
print(f"strip() - Removed whitespaces in left(Leading) and right(Trialing) - {name.strip()}")
print(f"lstrip() - Remove Leading whitespaces - {name.lstrip()} , rstrip() - Remove Trialing whitespaces - {name.rstrip()}")
print(f"capitalize() - Capitalize the first value of the string - {name.capitalize()}")
print(f"title() - Capitalize the first letter of each word - {name.title()}")
print(f"split() returns List - Splits the string based on a separator(\" \") - {name.split(" ")}")
