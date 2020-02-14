# Github: EchTR



# [--- Messages ---]
d_desteklenmeyen_k = "We currently only support the Latin alphabet."
d_s_cozulmus = "Decrypted version: "
d_sifrelenmis = "Encrypted version: "
# [---          ---]

encrypt("echtr")
decrypt("echtr")

def encrypt(metin):
	sifrelenmis = ""
	desteklenmeyen = 0
	for i in metin:
		if (i.lower() == "a"):
			sifrelenmis = (sifrelenmis + "z")
		elif (i.lower() == "."):
			sifrelenmis = (sifrelenmis + ".")
		elif (i.lower() == "!"):
			sifrelenmis = (sifrelenmis + "!")
		elif (i.lower() == "$"):
			sifrelenmis = (sifrelenmis + "$")
		elif (i.lower() == ","):
			sifrelenmis = (sifrelenmis + ",")
		elif (i.lower() == "="):
			sifrelenmis = (sifrelenmis + "=")
		elif (i.lower() == "?"):
			sifrelenmis = (sifrelenmis + "?")
		elif (i.lower() == "*"):
			sifrelenmis = (sifrelenmis + "*")
		elif (i.lower() == "-"):
			sifrelenmis = (sifrelenmis + "-")
		elif (i.lower() == "}"):
			sifrelenmis = (sifrelenmis + "}")
		elif (i.lower() == "{"):
			sifrelenmis = (sifrelenmis + "{")
		elif (i.lower() == "("):
			sifrelenmis = (sifrelenmis + "(")
		elif (i.lower() == ")"):
			sifrelenmis = (sifrelenmis + ")")
		elif (i.lower() == "["):
			sifrelenmis = (sifrelenmis + "[")
		elif (i.lower() == "]"):
			sifrelenmis = (sifrelenmis + "]")
		elif (i.lower() == "/"):
			sifrelenmis = (sifrelenmis + "/")
		elif (i.lower() == "&"):
			sifrelenmis = (sifrelenmis + "&")
		elif (i.lower() == "%"):
			sifrelenmis = (sifrelenmis + "%")
		elif (i.lower() == "½"):
			sifrelenmis = (sifrelenmis + "½")
		elif (i.lower() == "+"):
			sifrelenmis = (sifrelenmis + "+")
		elif (i.lower() == "#"):
			sifrelenmis = (sifrelenmis + "#")
		elif (i.lower() == "^"):
			sifrelenmis = (sifrelenmis + "^")
		elif (i.lower() == "'"):
			sifrelenmis = (sifrelenmis + "'")
		elif (i.lower() == "£"):
			sifrelenmis = (sifrelenmis + "£")
		elif (i.lower() == "!"):
			sifrelenmis = (sifrelenmis + "£")
		elif (i.lower() == " "):
			sifrelenmis = (sifrelenmis + " ")
		elif (i.lower() == "b"):
			sifrelenmis = (sifrelenmis + "y")
		elif (i.lower() == "c"):
			sifrelenmis = (sifrelenmis + "x")
		elif (i.lower() == "d"):
			sifrelenmis = (sifrelenmis + "w")
		elif (i.lower() == "e"):
			sifrelenmis = (sifrelenmis + "v")
		elif (i.lower() == "f"):
			sifrelenmis = (sifrelenmis + "u")
		elif (i.lower() == "g"):
			sifrelenmis = (sifrelenmis + "t")
		elif (i.lower() == "h"):
			sifrelenmis = (sifrelenmis + "s")
		elif (i.lower() == "i"):
			sifrelenmis = (sifrelenmis + "r")
		elif (i.lower() == "j"):
			sifrelenmis = (sifrelenmis + "q")
		elif (i.lower() == "k"):
			sifrelenmis = (sifrelenmis + "p")
		elif (i.lower() == "l"):
			sifrelenmis = (sifrelenmis + "o")
		elif (i.lower() == "m"):
			sifrelenmis = (sifrelenmis + "n")
		elif (i.lower() == "n"):
			sifrelenmis = (sifrelenmis + "m")
		elif (i.lower() == "o"):
			sifrelenmis = (sifrelenmis + "l")
		elif (i.lower() == "p"):
			sifrelenmis = (sifrelenmis + "k")
		elif (i.lower() == "q"):
			sifrelenmis = (sifrelenmis + "j")
		elif (i.lower() == "r"):
			sifrelenmis = (sifrelenmis + "i")
		elif (i.lower() == "s"):
			sifrelenmis = (sifrelenmis + "h")
		elif (i.lower() == "t"):
			sifrelenmis = (sifrelenmis + "g")
		elif (i.lower() == "u"):
			sifrelenmis = (sifrelenmis + "f")
		elif (i.lower() == "v"):
			sifrelenmis = (sifrelenmis + "e")
		elif (i.lower() == "w"):
			sifrelenmis = (sifrelenmis + "d")
		elif (i.lower() == "x"):
			sifrelenmis = (sifrelenmis + "c")
		elif (i.lower() == "y"):
			sifrelenmis = (sifrelenmis + "b")
		elif (i.lower() == "z"):
			sifrelenmis = (sifrelenmis + "a")
		else:
			desteklenmeyen = desteklenmeyen + 1
	if (desteklenmeyen >= 1):
		print(d_desteklenmeyen_k)
	else:
		print("Şifrelenmiş hali: " + sifrelenmis)
def decrypt(metin):
	c = 0
	desteklenmeyen = 0
	sifresi_cozulmus = ""
	uzunluk = len(metin)
	if (1 == 2): # uzunluk % 2 != 0
		c = 0
	else:
		for i in metin:
			if (i.lower() == "z"):
				sifresi_cozulmus = (sifresi_cozulmus + "a")
			elif (i.lower() == "."):
				sifresi_cozulmus = (sifresi_cozulmus + ".")
			elif (i.lower() == "!"):
				sifresi_cozulmus = (sifresi_cozulmus + "!")
			elif (i.lower() == " "):
				sifresi_cozulmus = (sifresi_cozulmus + " ")
			elif (i.lower() == ","):
				sifresi_cozulmus = (sifresi_cozulmus + ",")
			elif (i.lower() == "="):
				sifresi_cozulmus = (sifresi_cozulmus + "=")
			elif (i.lower() == "?"):
				sifresi_cozulmus = (sifresi_cozulmus + "?")
			elif (i.lower() == "*"):
				sifresi_cozulmus = (sifresi_cozulmus + "*")
			elif (i.lower() == "-"):
				sifresi_cozulmus = (sifresi_cozulmus + "-")
			elif (i.lower() == "}"):
				sifresi_cozulmus = (sifresi_cozulmus + "}")
			elif (i.lower() == "{"):
				sifresi_cozulmus = (sifresi_cozulmus + "{")
			elif (i.lower() == "("):
				sifresi_cozulmus = (sifresi_cozulmus + "(")
			elif (i.lower() == ")"):
				sifresi_cozulmus = (sifresi_cozulmus + ")")
			elif (i.lower() == "["):
				sifresi_cozulmus = (sifresi_cozulmus + "[")
			elif (i.lower() == "]"):
				sifresi_cozulmus = (sifresi_cozulmus + "]")
			elif (i.lower() == "/"):
				sifresi_cozulmus = (sifresi_cozulmus + "/")
			elif (i.lower() == "&"):
				sifresi_cozulmus = (sifresi_cozulmus + "&")
			elif (i.lower() == "%"):
				sifresi_cozulmus = (sifresi_cozulmus + "%")
			elif (i.lower() == "½"):
				sifresi_cozulmus = (sifresi_cozulmus + "½")
			elif (i.lower() == "+"):
				sifresi_cozulmus = (sifresi_cozulmus + "+")
			elif (i.lower() == "#"):
				sifresi_cozulmus = (sifresi_cozulmus + "#")
			elif (i.lower() == "^"):
				sifresi_cozulmus = (sifresi_cozulmus + "^")
			elif (i.lower() == "'"):
				sifresi_cozulmus = (sifresi_cozulmus + "'")
			elif (i.lower() == "£"):
				sifresi_cozulmus = (sifresi_cozulmus + "£")
			elif (i.lower() == "!"):
				sifresi_cozulmus = (sifresi_cozulmus + "£")
			elif (i.lower() == "$"):
				sifresi_cozulmus = (sifresi_cozulmus + "$")
			elif (i.lower() == "y"):
				sifresi_cozulmus = (sifresi_cozulmus + "b")
			elif (i.lower() == "x"):
				sifresi_cozulmus = (sifresi_cozulmus + "c")
			elif (i.lower() == "w"):
				sifresi_cozulmus = (sifresi_cozulmus + "d")
			elif (i.lower() == "v"):
				sifresi_cozulmus = (sifresi_cozulmus + "e")
			elif (i.lower() == "u"):
				sifresi_cozulmus = (sifresi_cozulmus + "f")
			elif (i.lower() == "t"):
				sifresi_cozulmus = (sifresi_cozulmus + "g")
			elif (i.lower() == "s"):
				sifresi_cozulmus = (sifresi_cozulmus + "h")
			elif (i.lower() == "r"):
				sifresi_cozulmus = (sifresi_cozulmus + "i")
			elif (i.lower() == "q"):
				sifresi_cozulmus = (sifresi_cozulmus + "j")
			elif (i.lower() == "p"):
				sifresi_cozulmus = (sifresi_cozulmus + "k")
			elif (i.lower() == "o"):
				sifresi_cozulmus = (sifresi_cozulmus + "l")
			elif (i.lower() == "n"):
				sifresi_cozulmus = (sifresi_cozulmus + "m")
			elif (i.lower() == "m"):
				sifresi_cozulmus = (sifresi_cozulmus + "n")
			elif (i.lower() == "l"):
				sifresi_cozulmus = (sifresi_cozulmus + "o")
			elif (i.lower() == "k"):
				sifresi_cozulmus = (sifresi_cozulmus + "p")
			elif (i.lower() == "j"):
				sifresi_cozulmus = (sifresi_cozulmus + "q")
			elif (i.lower() == "i"):
				sifresi_cozulmus = (sifresi_cozulmus + "r")
			elif (i.lower() == "h"):
				sifresi_cozulmus = (sifresi_cozulmus + "s")
			elif (i.lower() == "g"):
				sifresi_cozulmus = (sifresi_cozulmus + "t")
			elif (i.lower() == "f"):
				sifresi_cozulmus = (sifresi_cozulmus + "u")
			elif (i.lower() == "e"):
				sifresi_cozulmus = (sifresi_cozulmus + "v")
			elif (i.lower() == "d"):
				sifresi_cozulmus = (sifresi_cozulmus + "w")
			elif (i.lower() == "c"):
				sifresi_cozulmus = (sifresi_cozulmus + "x")
			elif (i.lower() == "b"):
				sifresi_cozulmus = (sifresi_cozulmus + "y")
			elif (i.lower() == "a"):
				sifresi_cozulmus = (sifresi_cozulmus + "z")
			else:
				desteklenmeyen = desteklenmeyen + 1
		if (desteklenmeyen >= 1):
			print(d_desteklenmeyen_k)
		else:
			print(d_s_cozulmus + sifresi_cozulmus)
