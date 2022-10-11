# github.com/echtr

notlar = {
    "Öğrenci 1": 90,
    "Öğrenci 2": 80,
    "Öğrenci 3": 85,
    "Öğrenci 4": 80
}

# notu 85 veya 85'i geçen öğrenciler takdir alır.

# klasik yöntem:
print("(Klasik Yöntem) Takdir Alabilenler: ")
for i in notlar.items():
    if i[1] >= 85: print(i[0])

# lambda yöntemi
print("\n(Lambda Yöntemi) Takdir Alabilenler:")
print(dict(filter(lambda i: i[1]>=85, notlar.items())))
