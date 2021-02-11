sayi = int(input("Faktoriyeli alınacak sayı: " ))

faktoriyel = 1
sayici = 1

while sayi+1 > sayici:
    faktoriyel = faktoriyel *sayici
    sayici+=1

print(faktoriyel)