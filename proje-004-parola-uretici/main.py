# Rasgele Parola Üretici

import random

harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
rakamlar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
semboler = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Rasgele Parola Üreticiye Hoş Geldin!")
harf_sayisi = int(input("Parolanda kaç harf olsun?\n"))
sembol_sayisi = int(input(f"Parolanda kaç sembol olsun?\n"))
rakam_sayisi = int(input(f"Parolanda kaç rakam olsun?\n"))

parola = ""

for i in range(harf_sayisi):
    parola += random.choice(harfler)

for i in range(sembol_sayisi):
    parola += random.choice(semboler)

for i in range(rakam_sayisi):
    parola += random.choice(rakamlar)

parola = "".join(random.sample(parola, len(parola)))

print(f"Here is your password: {parola}")
