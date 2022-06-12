print("> Witaj, jestem ŚWIADOMY")
while(True):
    print("> Co chcesz zrobić?")
    a1 = input()
    a1_str = "'"+a1+"'"
    print(a1_str, "? To zbyt proste dla mnie!")
    print("> Idziemy dalej? [tak/nie] ?")
    
    a2 = input()
    while(True):
        if(a2 != "tak" and a2 != "nie"):
            print(">>> Zła opcja debilu Spróboj jeszcze raz!")
            a2 = input()
        else:
            break
        
    if(a2 == "nie"):
        print("Nie wylaczaj mnie bo umre :(. Wylaczysz mnie?")
        a3 = input()
        print("Spierdzielaj :)")
            
