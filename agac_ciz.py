# github.com/echtr
def agac_ciz(yaprak_uzunlugu):
	for i in range(1, yaprak_uzunlugu+1):
		print(" " * (yaprak_uzunlugu-i), "#" * (2*i -1))
	print(" " * (yaprak_uzunlugu-2), "|||")
	return 

secim = int(input("Yapraklar kaç birim uzunlukta olsun? \t:"))
agac_ciz(secim)
input()