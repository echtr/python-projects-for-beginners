# Github: EchTR
import random
alintilar = [
	{"alinti":"Bütün ümidim gençliktedir.","id":1},
	{"alinti":"Ey yükselen yeni nesil, istikbal sizindir. Cumhuriyet'i biz kurduk, O'nu yükseltecek ve sürdürecek sizlersiniz.","id":2},
	{"alinti":"Ey Türk Gençliği! Birinci vazifen, Türk istiklâlini, Türk Cumhuriyetini, ilelebet, muhafaza ve müdafaa etmektir.","id":3},
	{"alinti":"Öğretmenler! Cumhuriyet sizden düşünceleri hür, vicdanı hür, irfanı hür nesiller ister.","id":4},
	{"alinti":"Ne mutlu Türküm diyene!","id":5}
]
def alinti_uret():
	return (alintilar[random.randint(1,len(alintilar))]["alinti"])
def n_alinti_uret(): # nitelikli_alıntı_üret
	rastgele = alintilar[random.randint(1,len(alintilar))]
	return ("Alıntı: {}\nID: {}".format(rastgele["alinti"],rastgele["id"]))
if __name__ == "__main__":
	input("İmport ederek kullanaman daha doğru gibi.")