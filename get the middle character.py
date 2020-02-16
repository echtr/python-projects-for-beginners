# Github: EchTR
def get_middle(yazi):
	uzunluk = int(len(yazi))
	if uzunluk % 2 == 0:
		bolum = int(uzunluk / 2)
		return yazi[bolum-1:bolum+1]
	elif uzunluk % 2 == 1:
		bolum = int(uzunluk / 2)
		return yazi[bolum:bolum+1]
input(get_middle("tete"))