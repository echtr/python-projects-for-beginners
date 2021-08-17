# github.com/echtr
import time
import os
def olustur(liste_uzunluk):
	veri = [1,1]
	for i in range(liste_uzunluk):
		veri.append(veri[-1] + veri[-2])
		print(veri)
		time.sleep(0.3)
		os.system("cls")
	print(veri)

if __name__ == "__main__":
	ne_kadar = int(input("Fibonacci listesinin uzunluğu ne kadar olsun? \t:"))
	olustur(ne_kadar)
	input()