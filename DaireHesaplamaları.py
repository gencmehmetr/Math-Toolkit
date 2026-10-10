## Daire Alanı ve Çevresini Hesaplama Programı

def DaireHesaplamaları():
    print("\nDaire Hesaplamaları Programına Hoşgeldiniz")
    pi = 3.14159

    print("\nHerhangi bir Adımda Çıkmak İçin (q) harfini kullanabilirsiniz")

    while True:
        try:
            R = input("\nDairenin Çapını Giriniz: ")
            if R.lower() == "q":  ## lower() ın bu kullanımı önemli
                break
            R = float(R)
            r = R / 2

        except ValueError:
            print("Lütfen Bir Sayı Giriniz")
            continue

        if r < 0:
            print("Negatif Bir Sayı Girdiniz!")
            continue
        elif r == 0:
            print("Bu Bir Nokta")
            continue

        Alan = pi * r ** 2
        Çevre = 2 * pi * r

        basamak = int(2)

        print("Dairenin Alanı: %.*f " % (basamak,
                                         Alan))  # burdaki olay da önemli virgülden sonra kaç basamak gösterileceğini ayarlamak için
        print("Dairenin Çevresi: %.*f" % (basamak,
                                          Çevre))  # * olayı da önemli bu sayede kaç basamak gösterileceğini de girdi olarak alabiliriz

        devammı = input("Tekrar başlamak ister misiniz? (e/h)").lower()

        if devammı == "e":
            continue
        break
