# Boş bir sözlük oluşturarak notları saklayacağız
notlar = {}

def not_ekle():
    baslik = input("Not başlığını girin: ")
    icerik = input("Not içeriğini girin: ")
    notlar[baslik] = icerik
    print("Not başarıyla eklendi!")

def notlari_goruntule():
    if not notlar:
        print("Henüz hiç not eklenmedi.")
    else:
        print("Notlarınız:")
        for baslik, icerik in notlar.items():
            print(f"\n{baslik}:\n{icerik}")

def not_sil():
    baslik = input("Silmek istediğiniz notun başlığını girin: ")
    if baslik in notlar:
        del notlar[baslik]
        print(f"'{baslik}' başlıklı not silindi.")
    else:
        print("Bu başlıkta bir not bulunamadı.")

def ana_menu_goster():
    print("\n1. Not Ekle\n2. Notları Görüntüle\n3. Not Sil\n4. Çıkış")

while True:
    ana_menu_goster()
    secim = input("Yapmak istediğiniz işlemi seçin (1-4): ")

    if secim == '1':
        not_ekle()
    elif secim == '2':
        notlari_goruntule()
    elif secim == '3':
        not_sil()
    elif secim == '4':
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")