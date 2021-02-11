import requests
xssList=[]
dosya = open("XSS_List2.txt", "r")
icerik = dosya.read()
dosya.close()

header = {"Cookie": "ASP.NET_SessionId=oqrncsvn5h1i2m55l0yxvc45"}

for payload in icerik.splitlines():
    print(payload)
    url="http://www."+payload
    sonuc=requests.get(url=url, headers=header)
    if payload in sonuc.content():
       print("Muhtemel XSS var: " , payload)