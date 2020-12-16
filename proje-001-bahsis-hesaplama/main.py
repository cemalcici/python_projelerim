# Bahşis Hesaplama Programı

print("Bahşiş hesaplama programına hoş geldiniz!")

toplam_hesap = float(input("Toplam hesap ücreti nedir?\n"))
tip_orani = int(input("Bahşiş, hangi orana göre hesaplansın? (%10, %12, %15)\n"))
kisi_sayisi = int(input("Hesabı kaç kişi ödeyecek?\n"))

sonuc = (toplam_hesap / kisi_sayisi) * (1 + tip_orani / 100)

print(f"Kişi başı ödenecek ücret: {round(sonuc, 2)}₺'dir.")
