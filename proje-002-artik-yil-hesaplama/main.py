# Artık Yıl Hesaplama

yil = int(input("Yıl değerini giziniz:\t"))

if yil % 4 == 0:
    if yil % 100 == 0:
        if yil % 400 == 0:
            print("Artık yıl.")
        else:
            print("Artık yıl değil.")
    else:
        print("Artık yıl.")
else:
    print("Artık yıl değil.")
