from Dörtİşlem import *
from DaireHesaplamaları import *
from DiskriminantHesaplama import *
from SayıBilgisi import *
from ParçalıFonksiyon import *

while True:
    print("--- MATH TOOLKIT ANA MENÜ ---")
    print("1. Dört İşlem")
    print("2. Daire Hesaplamaları")
    print("3. Diskriminant Hesaplama")
    print("4. Sayı Bilgisi (Pozitif/Negatif/Sıfır)")
    print("5. Parçalı Fonksiyon")
    print("q. Çıkış")

    a = input("CEVABINIZ: ")

    if a == "q":
        break
    elif a == "1":
        Dörtİşlem()
        devammı9 = input("Ana Menüye Dönmek İster misiniz? (e/h)").lower()
        if devammı9 == "e":
            continue
        break
    elif a == "2":
        DaireHesaplamaları()
        devammı9 = input("Ana Menüye Dönmek İster misiniz? (e/h)").lower()
        if devammı9 == "e":
            continue
        break
    elif a == "3":
        DiskriminantHesaplama()
        devammı9 = input("Ana Menüye Dönmek İster misiniz? (e/h)").lower()
        if devammı9 == "e":
            continue
        break
    elif a == "4":
        SayıBilgisi()
        devammı9 = input("Ana Menüye Dönmek İster misiniz? (e/h)").lower()
        if devammı9 == "e":
            continue
        break
    elif a == "5":
        ParçalıFonksiyon()
        devammı9 = input("Ana Menüye Dönmek İster misiniz? (e/h)").lower()
        if devammı9 == "e":
            continue
        break


