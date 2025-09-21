senju_details = [
    {"name":"Hashirama", "status":"dead", "special_jutsu":"wood style and sage mode"},
    {"name":"Tobirama", "status":"dead", "special_jutsu":"flying thunder god and water style"},
    {"name":"Tsunade", "status":"alive", "special_jutsu":"medical jutsu"},
    {"name":"Nawaki", "status":"dead", "special_jutsu":"nothing"}
]

for senju in senju_details:
    print(f"{senju["name"]} is {senju["status"]} and is known for {senju["special_jutsu"]}.")