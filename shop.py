HP = 50
buy = False
medkit = 0
gold = 10000
ATK = 1
HPMAX = 50

def shop():
    global buy, gold, medkit, ATK, HPMAX

    while buy:
        print("Welcome to the shop!")
        print("GOLD: " + str(gold))
        print("mkits: " + str(medkit))
        print("ATK: " + str(ATK))
        print("1 - BUY POTION (30HP) - 5 GOLD")
        print("2 - UPGRADE WEAPON (+2ATK) - 10 GOLD")
        print("3 - UPGRADE HEALTH (+2HP - 15 GOLD)")
        print("4 - LEAVE")

        
        choice = input("# ")

        if choice == "1":
            if gold > 5:
                medkit += 1
                gold -= 5
                print("You've bought a potion!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "2":
            if gold > 10:
                ATK += 2
                gold -= 10
                print("You've upgraded your weapon!")
            else:
                print("Not enough gold!")
        elif choice == "3":
            if gold > 15:
                HPMAX += 5
                gold -= 15
                print("You've upgraded your HP!")
            else:
                print("Not enough gold!")
            input("> ")
        elif choice == "4":
            buy = False

buy = True
shop()
