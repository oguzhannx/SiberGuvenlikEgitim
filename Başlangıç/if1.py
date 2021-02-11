a_sinifi= ["Ahmet", "Mehmet"]
b_Sinifi= ["Ali", "Ayşe"]

isim= input("İsim Giriniz: ")

if isim in a_sinifi:
    print("Kişi a Sınıfıfında")
elif isim in b_Sinifi:
    print("Kişi b Sınıfıfında")
else:
    print("Böyle kişi bulunmamaktadır.")