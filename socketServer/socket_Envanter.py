import socket

port_List = []
banner_List = []

dosya = open("ip_List.txt", "r")
ipler = dosya.read()
dosya.close()

for ip in ipler.splitlines():
    print(f"Denenecek ip: {ip}")
    for port in range(1, 25):
        try:
            soket = socket.socket()
            soket.connect((str(ip), int(port)))
            banner = soket.recv(1024)  # SV bilgisi geri dönüşü
            banner_List.append(str(banner))
            port_List.append(str(port))
            socket.close()

            if "SSH" in str(banner):
                print("Sistem Linux veya network cihazı olabilir...")
                dosya = open("SSHList.txt", "a")
                log = ip + "\n"
                dosya.write(log)
                dosya.close()

        except:
            pass
print(banner_List)
print(port_List)
