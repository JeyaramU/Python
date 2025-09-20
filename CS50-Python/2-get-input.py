input ("Enter name ?")
print("Nothing happens here after getting the input")


# input() is only for string
name = input ("Enter name ?")

# print does not work like Java
print("Print does not work like Java log - {}",name)

# When multiple arguments are given to print function, it will add an additional space
print("Adding name like ,name as another argument adds an additional space in the print - ",name)
print("Your name is printed here - "+name)

# To pass like java log
print(f"Prefixing quotes with f tells python its a special string with variable inside {name}")