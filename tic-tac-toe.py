# github.com/echtr
import os

class tictactoe:
	def __init__(self, temp=0):
		self.temp = temp
		self.tahta = ["1", "2", "3",
				 "4", "5", "6",
				 "7", "8", "9"]
		self.sira = "X"
	def oyna(self):
		while True:
			if self.sira == "X":
				while True:
					print(" | ",self.tahta[0], " | ", self.tahta[1], " | ", self.tahta[2], " | ")
					print(" | ",self.tahta[3], " | ", self.tahta[4], " | ", self.tahta[5], " | ")
					print(" | ",self.tahta[6], " | ", self.tahta[7], " | ", self.tahta[8], " | ")
					soru = int(input("(X) Hangi bölüme oynamak isteriniz?\t:"))
					if soru <= 0 or soru > 9:
						print("Belirtilen aralıkta değer yazmalısın.")
						input()
						os.system("cls")
						
					else:
						if self.tahta[soru-1] == "X" or self.tahta[soru-1] == "Y":
							print("Orası dolu.")
							input()
							os.system("cls")
							
						else:
							self.tahta[soru-1] = "X"
							self.sira = "Y"
							os.system("cls")
							break
			else:
				while True:
					print(" | ",self.tahta[0], " | ", self.tahta[1], " | ", self.tahta[2], " | ")
					print(" | ",self.tahta[3], " | ", self.tahta[4], " | ", self.tahta[5], " | ")
					print(" | ",self.tahta[6], " | ", self.tahta[7], " | ", self.tahta[8], " | ")
					soru = int(input("(Y) Hangi bölüme oynamak isteriniz?\t:"))
					if soru <= 0 or soru > 9:
						print("Belirtilen aralıkta değer yazmalısın.")
						input()
						os.system("cls")
						
					else:
						if self.tahta[soru-1] == "X" or self.tahta[soru-1] == "Y":
							print("Orası dolu.")
							input()
							os.system("cls")
							
						else:
							self.tahta[soru-1] = "Y"
							self.sira = "X"
							os.system("cls")
							break

			if self.tahta[0] == "X" and self.tahta[1] == "X" and self.tahta[2] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[3] == "X" and self.tahta[4] == "X" and self.tahta[5] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[6] == "X" and self.tahta[7] == "X" and self.tahta[8] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[0] == "X" and self.tahta[3] == "X" and self.tahta[6] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[1] == "X" and self.tahta[4] == "X" and self.tahta[7] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[2] == "X" and self.tahta[5] == "X" and self.tahta[8] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[0] == "X" and self.tahta[4] == "X" and self.tahta[8] == "X":
				input("X kazandı, oyun bitti.")
				break
			elif self.tahta[2] == "X" and self.tahta[4] == "X" and self.tahta[6] == "X":
				input("X kazandı, oyun bitti.")
				break

			if self.tahta[0] == "Y" and self.tahta[1] == "Y" and self.tahta[2] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[3] == "Y" and self.tahta[4] == "Y" and self.tahta[5] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[6] == "Y" and self.tahta[7] == "Y" and self.tahta[8] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[0] == "Y" and self.tahta[3] == "Y" and self.tahta[6] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[1] == "Y" and self.tahta[4] == "Y" and self.tahta[7] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[2] == "Y" and self.tahta[5] == "Y" and self.tahta[8] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[0] == "Y" and self.tahta[4] == "Y" and self.tahta[8] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			elif self.tahta[2] == "Y" and self.tahta[4] == "Y" and self.tahta[6] == "Y":
				input("Y kazandı, oyun bitti.")
				break
			sayac = 0
			for karakter in self.tahta:
				if karakter == "X" or karakter == "Y":
					sayac += 1
			if sayac == 9:
				print("Oyun berabere.")
				break
if __name__ == "__main__":
	oyun = tictactoe()
	oyun.oyna()
	input()