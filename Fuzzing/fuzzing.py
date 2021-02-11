import requests
from urllib3.util import url

dosya = open("fuzzing.txt", "r")
icerik = dosya.read()
dosya.close()
header = {"Cookie": "ASP.NET_SessionId=r5nwj3vfu2tgbozqp2cu1e45"}


for i in icerik.splitlines():

    url = "https://obs.sdu.edu.tr" + i
    sonuc = requests.get(url=url, headers=header)

    if "200" in str(sonuc.status_code):
        print("Dosya veya Dizin var:  " + (url + i))
    # else:
    #     print("Dosya veya dizin yok" + i)
