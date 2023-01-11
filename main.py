import time

choix = input("entrez 1 pour un chronomètre "
              "\nentrez 2 pour un décompte "
              "\n-> ")
chronometre = False
decompte = False

if(choix == "1") :
    minutes = 0
    secondes = 1

    minutes = int(minutes)
    secondes = int(secondes)
    IsOver = False

    while (IsOver == False):
        print("")
        print("")
        print(str(minutes) + " minutes " +
            "\net " + str(secondes) + " secondes")
        secondes = secondes + 1
        if (secondes >= 60):
            minutes = minutes + 1
            secondes = 0
        elif (minutes >= 60) :
            IsOver = True
        else :
            nothing = True
        time.sleep(1)


elif(choix == "2") :
    minutes = 0
    secondes = 0
    minutes = input("entrez les minutes"
                    "\n(max : 60)-> ")
    secondes = input("entrez les secondes"
                     "\n(max : 60)-> ")
    minutes = int(minutes)
    secondes = int(secondes)
    IsOver = False

    while (IsOver == False):
        print("")
        print("")
        print(str(minutes) + " minutes " +
            "\net " + str(secondes) + " secondes")
        secondes = secondes - 1
        if (secondes <= -1):
            minutes = minutes - 1
            secondes = 59
        elif(secondes <= 0 and minutes <= 0) :
            IsOver = True
            time.sleep(1)
            print("")
            print("")
            print("0 minutes \net 0 secondes")
            print("")
            print("décompte fini !")
        else :
            nothing = True
        time.sleep(1)

else :
    print("relancez le script \net entrez 1 ou 2")
