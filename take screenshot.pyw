# Github: EchTR
from tkinter import *
import pyautogui
import datetime
def goruntuAl():
	ekran_alintisi = pyautogui.screenshot()
	suan = datetime.datetime.now()
	ekrangoruntusu_adi = str(str(suan.year) + "-" + str(suan.month) + "-" + str(suan.day) + "-" + str(suan.hour) + "-" + str(suan.minute) + "-" + str(suan.second))
	ekran_alintisi.save("C:/Users/Public/Documents/screenshot{}.png".format(ekrangoruntusu_adi)) # You can edit.
pencere = Tk()
pencere.geometry("142x32")
uiButton1 = Button(pencere, text = "Take a Screenshot", command=goruntuAl, bg="green", fg = "white",font=10)
uiButton1.pack()
pencere.mainloop()
