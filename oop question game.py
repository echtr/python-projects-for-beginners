# Github: EchTR
import os
print("Welcome! My Github name is EchTR")
input("")
os.system("cls")
class soruSor:
	def __init__ (self,soruNum,soruIcerik,soruCevap):
		self.soruNum = soruNum
		self.soruIcerik = soruIcerik
		self.soruCevap = soruCevap
	def soruGoster(self):
		print("{} - {} : ".format(self.soruNum,self.soruIcerik))
		cevap = input("Answer: ")
		if (cevap.lower() == self.soruCevap.lower()):
			print("Correct!")
		elif (cevap == ""):
			print("Field cannot be empty!")
		else:
			print("Wrong!")
		input("")
		os.system("cls")	
soru1 = {"Soru":"Who is the founder of the Republic of Turkey ? [Mustafa Kemal Atatürk , Osman Bey]","Cevap":"Mustafa Kemal Atatürk","Numara":"1"}
soru2 = {"Soru":"In which programming language is this program written? [Python, C#]","Cevap":"Python","Numara":"2"}
soru3 = {"Soru":"What is my Github name ? [EchTR, imEch]","Cevap":"EchTR","Numara":"3"}
soru4 = {"Soru":"Which is different? [4,4,5,4]","Cevap":"5","Numara":"4"}
soru5 = {"Soru":"Do you like the game? [Yes, Yes]","Cevap":"Yes","Numara":"5"}
sorular = [soru1,soru2,soru3,soru4,soru5]
for i in sorular:
	soruKalibi = soruSor(i.get("Numara"),i.get("Soru"),i.get("Cevap"))
	soruKalibi.soruGoster()
