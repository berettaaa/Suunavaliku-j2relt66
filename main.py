from datetime import datetime
import math

#Teen logi mis salvestab ära kasutaja poolt sisestatud nime ja perekonnanime ning loob uue faili kuhu sisse see salvestatakse koos sisestamis kuupäevaga.

def salvesta_logi():
    eesnimi = input("Sisesta eesnimi: ")
    perenimi = input("Sisesta perekonnanimi: ")

    kuupaev = datetime.now().strftime("%Y-%m-%d")

    fail = open("logi.txt", "a", encoding="utf-8")
    fail.write(eesnimi + " " + perenimi + " - " + kuupaev + "\n")
    fail.close()

    print("Andmed salvestatud.")
    
 #Teen kalkulaatori mis lahendab ära Liitmise,lahutamise,korrutamise,jagamise ja pythagorose teoreemi ja tagastab selle kasutajala.

def kalkulaator():
    print("Vali tehe:")
    print("1 - Liitmine")
    print("2 - Lahutamine")
    print("3 - korrutamine")
    print("4 - Jagamine")
    print("5 - Pythagorose teoreem")

    valik = input("Valik: ")

    if valik == "5":
        a = float(input("Sisesta külg a: "))
        b = float(input("Sisesta külg b: "))
        c = math.sqrt(a * a + b * b)
        print("Hüpotenuus =", round(c, 2))
        return

    a = float(input("Sisesta esimene arv: "))
    b = float(input("Sisesta teine arv:"))

    if valik == "1":
        print("Tulemus:",a + b)
    elif valik == "2":
        print("Tulemus:",a - b)
    elif valik == "3":
        print("Tulemus:",a * b)
    elif valik == "4":
        if b == 0:
            print("nulliga ei saa jagada!")
        else:
            print("Tulemus:",a / b)
    else:
        print("Vale valik.")

def joonista_kolmnurk():
    kõrgus = int(input("Sisesta kolmnurga kõrgus: "))
    laius = int(input("Sisesta kolmnurga laius: "))

    i = 0
    vastus = (kõrgus,laius)
    while i < kõrgus:
        print("_"* laius)

    l = 0
    vastus = (kõrgus,laius)
    while l < laius:
        print("/"* kõrgus) #läks see lahendus käik meelest loodan et loogika, on õige
       
#teen endale menüü kust kasutaja saab valida millist asja ta kasutada soovib.
def menuu():
    while True:
        print()
        print("MENÜÜ")
        print("1 - Salvesta kasutaja andmed")
        print("2 - Kalkulaator")
        print("3 - Joonista kolmnurk")
        print("4 - Välju")

        valik = input("Valik: ")

        if valik == "1":
            salvesta_logi()
        elif valik == "2":
            kalkulaator()
        elif valik == "3":
            joonista_kolmnurk()
        elif valik == "4":
            break
        else:
            print("Vale valik.")


menuu()
    

    



    
    




