# Github: EchTR
def getCount(yazi):
	unlu_harfler = 0
	for i in yazi:
		if i.lower() in "aeiou":
			unlu_harfler = unlu_harfler + 1
	return unlu_harfler
input(get_count("efe"))