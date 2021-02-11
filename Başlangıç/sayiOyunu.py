import random

rnd = round(random.random()*100)
print("Sayı: ", rnd)
girilenSayi = int(input("0-100 arası bir sayı giriniz: "))

while rnd != girilenSayi:
    if girilenSayi > rnd:
        girilenSayi= int(input("Küçük bir sayı giriniz: "))
    else:
        girilenSayi= int(input("Büyük bir sayı giriniz: "))
    if girilenSayi == rnd:
        print("Tebrikler....    :D")
   


