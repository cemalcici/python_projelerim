# Taş Kağıt Makas Oyunu

import random
import os

tas = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

kagit = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

makas = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

kullanici = [tas, kagit, makas]
cpu = kullanici.copy()
yeniden = True

while yeniden:
    print("Taş-Kağıt-Makas Oyununa Hoş Geldin! Seçimini yap!")
    secenek = int(input("0-->Taş, 1-->Kağıt, 2-->Makas\n"))
    if 0 <= secenek < 3:
        kullanici_secimi = kullanici[secenek]
        cpu_secimi = cpu[random.randint(0, 2)]
        print(kullanici_secimi)
        print(f"Bilgisayarın seçimi:\n{cpu_secimi}")

        if kullanici_secimi == kullanici[0] and cpu_secimi == cpu[0]:
            print("Berabere.")  # taş - taş
        elif kullanici_secimi == kullanici[0] and cpu_secimi == cpu[1]:
            print("Kaybettin.")  # taş - kağıt
        elif kullanici_secimi == kullanici[0] and cpu_secimi == cpu[2]:
            print("Kazandın.")  # taş - makas
        elif kullanici_secimi == kullanici[1] and cpu_secimi == cpu[0]:
            print("Kazandın.")  # kağıt - taş
        elif kullanici_secimi == kullanici[1] and cpu_secimi == cpu[1]:
            print("Berabere.")  # kağıt - kağıt
        elif kullanici_secimi == kullanici[1] and cpu_secimi == cpu[2]:
            print("Kaybettin.")  # kağıt - makas
        elif kullanici_secimi == kullanici[2] and cpu_secimi == cpu[0]:
            print("Kaybettin.")  # makas - taş
        elif kullanici_secimi == kullanici[2] and cpu_secimi == cpu[1]:
            print("Kazandın.")  # makas - kağıt
        elif kullanici_secimi == kullanici[2] and cpu_secimi == cpu[2]:
            print("Berabere.")  # makas - makas

    else:
        print("Hatalı giriş yaptın.")

    s = input("Yeniden oynamak istiyor musun? 'evet' veya 'hayır' yaz.\n")
    if s.lower() != "evet":
        yeniden = False
    os.system("cls")


print("Oynadığın için teşekkürler!")
