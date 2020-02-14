# Github: EchTR
email = input("E-Mail:")
e_s = 0
n_s = 0
b_s = 0
ks_n = 0
e_y = 0
donus = 0
for i in email:
	donus = donus + 1
	if (i == "@"):
		e_s = e_s + 1
		e_y = donus
	elif (i == "."):
		n_s = n_s + 1
		ks_n = ks_n + 1
	elif (i == " "):
		b_s = b_s + 1
if(b_s != 0):
	print("There can be no space in the e-mail address!")
else:
	if (e_s == 0 or n_s == 0):
		print("Please enter a valid e-mail address!")
	elif (e_s > 1):
		print("Please put a '@' sign.")
	else:
		if(email[0] == "@" or email[e_y] == "."):
			print("Please enter a valid e-mail address!")	
		else:
			print(
				"""
				 E-Mail Properties
				[------------------]
				Length: {}
				Number of Dots: {}
				Shattered version: {} - @ - {}
				""".format(len(email), ks_n, email[0:e_y-1], email[e_y:len(email)]))
input("")
