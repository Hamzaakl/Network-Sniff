from scapy.all import *

def sniffPckt(pkct):
    pkct.sjow()

def start_sniff():
    scapy_sniff = sniff(prn = sniffPckt,timeout=5,iface='eth0',stop_filter=lambda x:x.haslayer(ICMP))
    wrpcap('Sum.pcap',scapy_sniff)

def start_read():
    scapyCap =rdpcap('Sum.pcap')
    ip_List = []
    for p in scapyCap:
        if IP in p:
            if p[IP].src not in ip_List:
                ip_List.append(p[IP].src)
        else:
            p.show()
    print(ip_List)


print("""
      1: sniff
      2: read
    """)

choice = input(">> ")

if (choice == 1):
    start_sniff()
elif (choice == 2):
    start_read()
else:
    print("Hatali Giris")     




