veri = "Eğitim 101"
egitim = list(veri)

print(egitim)

harfSayaci = 0
rakamSayaci = 0
for i in egitim:
    if str(i).isdecimal():
        rakamSayaci+=1
    else:
        harfSayaci+=1

print("Harf sayısı: ", harfSayaci)
print("Rakam sayısı: ", rakamSayaci)
