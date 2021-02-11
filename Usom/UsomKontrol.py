from tkinter import  *
import datetime

def kontrolEt():
    dosya= open("usom.txt", "r")
    icerik = dosya.read()
    dosya.close()
    ip = entry1.get()
    bugun = datetime.datetime.now()
    if str(ip) in icerik:
        dosya = open("log.txt", "a")
        yazi = str(ip + "zararli \n tarih: " + str(bugun) + "\n")
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlıdır")
    else:
        dosya = open("log.txt", "a")
        yazi = str(ip + "zararli degil\ntarih: " + str(bugun) + "\n")
        dosya.write(yazi)
        dosya.close()
        v.set("IP zararlı değil")



top= Tk()
top.title("Usom ip kontrol")

B = Button(top, text = "Kontrol Et", command = kontrolEt)
B.place(x=50, y=60)
B.pack()

label = Label(top, text="Kontrol edilecek ip yazınınz:")
label.place(x=50,y=80)
label.pack()

# entry = Entry(top)
entry1= Entry(top)
entry1.place(x=50, y=90)
entry1.pack()

v = StringVar()
label2 = Label(top, textvariable=v)
label2.place(x=50,y=100)
label2.pack()

top.mainloop()