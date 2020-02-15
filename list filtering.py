# Github: EchTR
def filter_list(liste):
	sayilar = []
	for i in liste:
		if(type(i) == int):
			sayilar.append(i)
	return sayilar
input(filter_list([1,2,"efe",20]))