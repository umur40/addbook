
# Kütüphane Yönetim Sistemi

class Kitap:
    def __init__(self, isim, yazar, yil):
        self.isim = isim
        self.yazar = yazar
        self.yil = yil
        self.odunc = False

class Kutuphane:
    def __init__(self):
        self.kitaplar = []
    
    def kitap_ekle(self):
        isim = input("Kitap adı: ")
        yazar = input("Yazar adı: ")
        while True:
            try:
                yil = int(input("Basım yılı: "))
                break
            except ValueError:
                print("Lütfen geçerli bir yıl girin!")
        
        yeni_kitap = Kitap(isim, yazar, yil)
        self.kitaplar.append(yeni_kitap)
        print(f"\n'{isim}' kitabı başarıyla eklendi!")
    
    def kitaplari_listele(self):
        if not self.kitaplar:
            print("\nKütüphanede hiç kitap yok!")
            return
        
        print("\nKütüphanedeki Kitaplar:")
        print("-" * 50)
        for i, kitap in enumerate(self.kitaplar, 1):
            durum = "Ödünç Verildi" if kitap.odunc else "Mevcut"
            print(f"{i}. {kitap.isim} - {kitap.yazar} ({kitap.yil}) - Durum: {durum}")
        print("-" * 50)
    
    def kitap_sil(self):
        self.kitaplari_listele()
        if not self.kitaplar:
            return
        
        while True:
            try:
                secim = int(input("\nSilmek istediğiniz kitabın numarasını girin: "))
                if 1 <= secim <= len(self.kitaplar):
                    silinen = self.kitaplar.pop(secim - 1)
                    print(f"\n'{silinen.isim}' kitabı başarıyla silindi!")
                    break
                else:
                    print("Geçersiz kitap numarası!")
            except ValueError:
                print("Lütfen geçerli bir numara girin!")
    
    def kitap_odunc(self):
        self.kitaplari_listele()
        if not self.kitaplar:
            return
        
        while True:
            try:
                secim = int(input("\nÖdünç vermek/iade almak istediğiniz kitabın numarasını girin: "))
                if 1 <= secim <= len(self.kitaplar):
                    kitap = self.kitaplar[secim - 1]
                    kitap.odunc = not kitap.odunc
                    durum = "ödünç verildi" if kitap.odunc else "iade alındı"
                    print(f"\n'{kitap.isim}' kitabı başarıyla {durum}!")
                    break
                else:
                    print("Geçersiz kitap numarası!")
            except ValueError:
                print("Lütfen geçerli bir numara girin!")

def ana_menu():
    kutuphane = Kutuphane()
    
    while True:
        print("\nKütüphane Yönetim Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Sil")
        print("4. Kitap Ödünç Ver/İade Al")
        print("5. Çıkış")
        
        secim = input("\nYapmak istediğiniz işlemi seçin (1-5): ")
        
        if secim == "1":
            kutuphane.kitap_ekle()
        elif secim == "2":
            kutuphane.kitaplari_listele()
        elif secim == "3":
            kutuphane.kitap_sil()
        elif secim == "4":
            kutuphane.kitap_odunc()
        elif secim == "5":
            print("\nProgramdan çıkılıyor...")
            break
        else:
            print("\nGeçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    ana_menu()
