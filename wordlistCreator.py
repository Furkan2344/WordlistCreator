import wordlist

mins = int(input("Minimum Değer: "))
maxs = int(input("Maximum Değer: "))

icerik = input("Wordlistin içerisinde bulunacak karakterler: ")

dosyaadi = input("Dosya adı: ")


olustur = wordlist.Generator(icerik)

try:
    with open(dosyaadi,"a") as dosya:
        toplamKelime = 0
        for i in olustur.generate(mins,maxs):
            dosya.write(i)
            dosya.write("\n")
            toplamKelime += 1
        print("Toplam kelime sayısı: "+str(toplamKelime))

except ValueError:
    print("Lütfen düzgün değerler giriniz.")