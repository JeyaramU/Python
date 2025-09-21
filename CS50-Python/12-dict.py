# Dictionary - keys and values
senjustatus = {
    "Hashirama": "dead",
    "Tobirama": "dead",
    "Tsunade": "alive",
    "Nawaki": "dead"
    }

# By default on iterating a dictionary it prints all keys
for name in senjustatus:
    print(name)

# Iterating only using dict, improving the below commented code
# for name in senjus:
#    print(f"{name} is {senjustatus[name]}")
for senju in senjustatus:
    print(f"{senju} is {senjustatus[senju]}")

