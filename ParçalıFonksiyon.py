def ParçalıFonksiyon():
    print("\nParçalı Fonksiyon Hesaplayıcısına Hoşgeldiniz")
    print("\nKurallar:")
    print(" x < -2  için -> f(x) = x^3")
    print(" -2 <= x <= 2 için -> f(x) = 2x + 5")
    print(" x > 2   için -> f(x) = x^2 - 1")

    while True:
        try:
            x = input("\nx değerini giriniz (Çıkış için 'q'): ")
            if x.lower() == 'q':
                print("Parçalı fonksiyon hesaplayıcısından çıkılıyor...")
                break

            x = float(x)

        except ValueError:
            print("Lütfen bir sayı giriniz.")
            continue

        if x < -2:
            sonuç = x ** 3
            print("Sonuç (x < -2 kuralı uygulandı): ", sonuç)

        elif -2 <= x <= 2:
            sonuç = (2 * x) + 5
            print("Sonuç (-2 <= x <= 2 kuralı uygulandı): ", sonuç)

        else:
            sonuç = (x ** 2) - 1
            print("Sonuç (x > 2 kuralı uygulandı): ", sonuç)

        devammı = input("Devam Etmek İster misiniz? (e/h)").lower()
        if devammı == "e":
            continue
        break

