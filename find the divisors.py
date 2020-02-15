# Github: EchTR
def divisors(integer):
	bolenler = []
	for i in range(2,integer):
		if(integer % i == 0):
			bolenler.append(i)
	if (bolenler == []):
		return (str(integer) + " is prime")
	else:
		return bolenler
input(divisors(12))