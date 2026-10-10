
def Dörtİşlem():
    print("Bu uygulama girdiğiniz 2 sayı ile istediğiniz 4 işlemi yapmanızı sağlar.")

    while True:
        print("çıkmak için q harfine basabilirsiniz")

        try:
            a = input("1. sayıyı giriniz: ")
            if a == "q":
                break
            a = float(a)

            b = input("2. sayıyı giriniz: ")
            if b == "q":
                break
            b = float(b)  ## bunu sonra yazdık çünkü önce q nun da geçerli bir cevap olması gerekiyor

        except ValueError:
            print("Lütfen Sadece Sayı Giriniz")
            continue

        cevap = input("Hangi işlemi yapmak istersiniz?\nm=çarpma\nn=bölme\nc=toplama\nd=çıkarma\nCEVAP: ").lower()

        if cevap == "m":
            print(a * b)

        elif cevap == "n":
            if b == 0:
                print("HATA! Bir Sayı Sıfıra Bölünemez")
            else:
                print(a / b)

        elif cevap == "c":
            print(a + b)

        elif cevap == "d":
            print(a - b)

        else:
            print("Geçerli bir harf seçiniz")

        devam = input("Tekrar işlem yapmak ister misiniz (e/h) : ").lower()
        if devam == "e":
            continue
        break