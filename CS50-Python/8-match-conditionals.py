# Match conditional similar to switch case

print(" 1-Hashirama \n 2-Tobirama \n 3-Hiruzen \n 4-Minato \n 5-Tsunade \n 6-Kakashi \n 7-Naruto")
name = int(input("Enter hokage number from 1-7 to know their clan : "))

match name:
    case 1 | 2 | 5:
        print("Senju Clan")
    case 3:
        print("Sarutobi Clan")
    case 4:
        print("No clan")
    case 6:
        print("Hatake Clan")
    case 7:
        print("Uzumaki Clan")
        print("Veli ooru karangaluke poiruchi, apa Uchiha yenna thakkali thokka. Solradhuku onnum illa - FYI - Words in Tamil")