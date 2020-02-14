# Github: EchTR
import datetime
suanki_tarih = datetime.datetime.now()
gun_ismi = suanki_tarih.strftime("%A")
if(gun_ismi == "Monday"):
	gun_ismi = "Pazartesi"
elif(gun_ismi == "Tuesday"):
	gun_ismi = "Salı"
elif(gun_ismi == "Wednesday"):
	gun_ismi = "Çarşamba"
elif(gun_ismi == "Thursday"):
	gun_ismi = "Perşembe"
elif(gun_ismi == "Friday"):
	gun_ismi = "Cuma"
elif(gun_ismi == "Saturday"):
	gun_ismi = "Cumartesi"
elif(gun_ismi == "Sunday"):
	gun_ismi = "Pazar"
else:
	gun_ismi = "Sistem hatası!"
print("Tarih: {}/{}/{} - {}".format(suanki_tarih.year,suanki_tarih.month,suanki_tarih.day,gun_ismi))
lgs = datetime.datetime(2020,6,7)
kalan_gun = (lgs.day - suanki_tarih.day)
ay_gun = (lgs.month - suanki_tarih.month)
yil_gun = (lgs.year - suanki_tarih.year)
print("LGS'e {} gün kaldı.".format(kalan_gun + ay_gun*30 + yil_gun*365))
input("")
