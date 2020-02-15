# Github: EchTR
def likes(names):
	uzunluk = len(names)
	if (uzunluk == 0):
		return "no one likes this"
	elif (uzunluk == 1):
		return names[0] + " likes this"
	elif (uzunluk == 2):
		return names[0] + " and " + names[1] + " like this"
	elif (uzunluk == 3):
		return names[0] + ", " + names[1] + " and " + names[2] + " like this"
	elif (uzunluk >= 4):
		return names[0] + ", " + names[1] + " and " + str(uzunluk - 2) + " others like this"
input(likes(["EchTR"]))
