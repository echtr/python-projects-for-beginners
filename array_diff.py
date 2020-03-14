# Github: EchTR
def array_diff(array1, kaldirilacak):
	kalan = []
	if array1 == []:
		return array1
	elif kaldirilacak == []:
		return array1
	else:
		for i in array1:
			if i != kaldirilacak[0]:
				kalan.append(i)
		return kalan
print(array_diff([1,5,5,1,5],[5])) # Array1: Normal List, Array2: number or number to be removed from array 1
input("")