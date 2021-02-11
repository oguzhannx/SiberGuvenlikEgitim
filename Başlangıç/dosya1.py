dosya = open("Sayilar.txt", "a")
for i in range(1, 10, 1):
    veri = str(i) + "\n"
    dosya.write(veri)
    dosya.close