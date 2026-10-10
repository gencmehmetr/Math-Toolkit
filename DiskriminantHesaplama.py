# 2. dereceden denklem diskriminantı hesaplama programı

def DiskriminantHesaplama():
    print("Bu program istediğiniz 2. dereceden denklemin diskriminantını bulmanızı sağlar.")

    print("Şablon:  a.x^2 + b.x + c")

    while True:

        try:
            print("Sırasıyla Değerleri Giriniz:")
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
        except ValueError:
            print("Lütfen Bir Sayı Giriniz")
            continue

        print("Denkleminiz: ", "{}*x^2 + {}*x + {}".format(a, b, c))

        input("HESAPLA (enter a basın)")

        diskriminant = b * b - 4 * a * c

        print("DİSKRİMİNANT: ", diskriminant)
        devammı = input("Devam Etmek İster misiniz? (e/h)").lower()
        if devammı == "e":
            continue
        break
