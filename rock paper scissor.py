#Github: EchTR
#Steam ID: EchTR
#Discord Name: EchTR
import random
import os
secenekler = ["tas","kagit","makas"]
tas = secenekler[0]
kagit = secenekler[1]
makas = secenekler[2]

kazanma = 0
kaybetme = 0
berabere = 0
anahtar = 0
print("TURKISH LANGUAGE")
while anahtar == 0:
    print("""
Merhabalar, taş kağıt, makas oyununa hoş geldin. 
1 = 'TAŞ' 
2 = 'KAĞIT'
3 = 'MAKAS' 
4 = 'SKORLARI GÖR!'
q = 'ÇIKIŞ YAP'
""")
    secSun = input("Seçimin nedir ?: ")
    bil_secim = random.choice(secenekler)
    if secSun == "1":
        if bil_secim == tas:
            input("Oyun berabere! Bilgisayar taş aldı!")
            berabere = berabere + 1
            os.system("cls")
        elif bil_secim == kagit:
            input("Kaybettin! Bilgisayar kağıt aldı!")
            kaybetme = kaybetme + 1 
            os.system("cls")
        elif bil_secim == makas:
            input("Oyunu kazandın! Bilgisayar makas aldı!")
            kazanma = kazanma + 1
            os.system("cls")
        else:
            input("Bir rakam seçmelisin.")
            os.system("cls")
    if secSun == "2":
        if bil_secim == tas:
            input("Oyunu kazandın! Bilgisayar taş aldı!")
            kazanma = kazanma + 1
            os.system("cls")
        elif bil_secim == kagit:
            input("Oyun berabere! Bilgisayar kağıt aldı!")
            berabere = berabere + 1 
            os.system("cls")
        elif bil_secim == makas:
            input("Oyunu kazandın! Bilgisayar makas aldı!")
            kaybetme = kaybetme + 1
            os.system("cls")
        else:
            input("Bir rakam seçmelisin.")
            os.system("cls")
    if secSun == "3":
        if bil_secim == tas:
            input("Oyunu kaybettin! Bilgisayar taş aldı!")
            kaybetme = kaybetme + 1
            os.system("cls")
        elif bil_secim == kagit:
            input("Oyun kazandın! Bilgisayar kağıt aldı!")
            kazanma = kazanma + 1 
            os.system("cls")
        elif bil_secim == makas:
            input("Oyunu berabere! Bilgisayar makas aldı!")
            berabere = berabere + 1
            os.system("cls")
        else:
            input("Bir rakam seçmelisin.")
            os.system("cls")
    if secSun == "4":
        print("Kazanma: ", kazanma)
        print("Kaybetme: ",kaybetme)
        print("Berabere: ", berabere)
        input("")
        os.system("cls")
    if secSun == "q":
        anahtar = 1
        input("Çıkmak için 'enter' tuşuna tıkla.")
