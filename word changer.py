# Github: EchTR
import os
kelime1 = input("Değişecek kelime :")
kelime2 = input("Hangi kelimeyle değiştirilsin ? :")
metin = input("Metni yazın:")
kelimeler = metin.split()
donus = -1
metin2 = ""
for i in kelimeler:
	if (i.lower() == kelime1.lower()):
		donus = donus+1
		kelimeler[donus] = kelime2
for i in kelimeler:
	metin2 = metin2 + i + " " 
print(metin2)
input("")