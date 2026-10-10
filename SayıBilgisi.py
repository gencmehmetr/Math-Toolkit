def SayıBilgisi():
    print("Sayınız Hakkında Bilgi Edinin :)")

    def sayıbilgisi():

        if a < 0:
            print("Sayınız Negatif")
        elif a > 0:
            print("Sayınız Pozitif")
        elif a == 0:
            print("Sayınız Sıfır")

    while True:
        a = input("SAYINIZ: ")
        a = float(a)

        sayıbilgisi()


        devammı = input("Devam Etmek İster misiniz? (e/h)").lower()
        if devammı == "e":
            continue
        break