"""
From documentation

The print function in python takes the below arguments - 5 different parameters, infinite arguments as *objects

print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

*objects - Any number of objects
end='\n' - Means it takes an end or new line 
sep=' '  - Separator

sep, name, file, flush are named parameters and they are optional

"""
# Using in-build print
print("This is 1st print")
print("This is 2st print")

# Override print() - Passing custom parameters to print - no end
print("This is 1st print", end="")
print("This is 2st print")

# Override print() - Passing custom parameters to print - diff separator
print("Default separator","Hello","World")
print("Passing custom separator","Hello","World", sep="-")

# In a formatted string use {{ }} to denote {}
print(f"FYI - To print numbers in US style(1,000,000 etc) use f\"{{number:,}}\"")
print(f"{1000:,}")