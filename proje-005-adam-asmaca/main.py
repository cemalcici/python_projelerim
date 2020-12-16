import logolar
import kelimeler
import random

kelime_listem = kelimeler.var

secilen_kelime = random.choice(kelime_listem)
kelime_uzunlugu = len(secilen_kelime)
oyunu_bitir = False
hak = 6
print(logolar.logo)

gorunum = []
for sayi in range(kelime_uzunlugu):
    gorunum.append("_")

print("Adam Asmaca Oyununa Hoş Geldin! Bakalım aşağıdaki kelimeyi seni asmadan tahmin edebilecek misin?")

while not oyunu_bitir:
    print(gorunum)
    tahmin = input("Bir harf söyle\n").lower()

    if tahmin in gorunum:
        print("Bu harfi zaten önceden tahmin ettin. Yeni bir harf dene!")

    for indeks in range(kelime_uzunlugu):
        if secilen_kelime[indeks] == tahmin:
            gorunum[indeks] = secilen_kelime[indeks]

    if tahmin not in secilen_kelime:
        print(f"{tahmin} harfi kelimede yok. Bir hak kaybettin!")
        hak -= 1
        if hak == 0:
            oyunu_bitir = True
            print("Kaybettin.")
            print(f"Bilemediğin kelime {secilen_kelime}")

    if "_" not in gorunum:
        oyunu_bitir = True
        print("Kazandın.")
        print(f"{secilen_kelime} kelimesini tahmin etmeyi başardın!")

    print(logolar.stages[hak])