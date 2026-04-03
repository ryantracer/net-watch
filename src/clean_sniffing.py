import libs

def packet_tracer(packet):
    proto = None
    mac = None
   
    ip_flags = packet[libs.scapy.IP].flags if packet.haslayer(libs.scapy.IP) else None
    
    tcp_flags = packet[libs.scapy.TCP].flags if packet.haslayer(libs.scapy.TCP) else None
    
    if libs.scapy.IP in packet:
        print(f"From {libs.ANSI['GREEN']}{packet[libs.scapy.IP].src}{libs.ANSI['END']} to {libs.ANSI['GREEN']}{packet[libs.scapy.IP].dst}{libs.ANSI['END']}", end="")

        if packet.haslayer(libs.scapy.TCP):
            proto = 'TCP'
        elif packet.haslayer(libs.scapy.UDP):
            proto = 'UDP'
        elif packet.haslayer(libs.scapy.ICMP):
            proto = 'ICMP'
        else:
            proto = 'OTHER'
        
        print(f' - {proto}', end='')
    
        if packet.haslayer(libs.scapy.Ether):
            mac = packet[libs.scapy.Ether].src

        print(f' - {mac}', end='')
        
        if proto == 'TCP':
            print(f' - TCP flags: {tcp_flags}', end='')
        
        if ip_flags != None:
            print(f' - IP flags: {ip_flags}')



def sniffing(iface=None, filter=None, count=None, timeout=None, write=False):
    kwargs = {
            "prn": packet_tracer
            }
    if iface:
        kwargs["iface"] = iface
    if filter:
        kwargs["filter"] = filter
    if count is not None:
        kwargs["count"] = count
    if timeout is not None:
        kwargs["timeout"] = timeout
    
    libs.scapy.sniff(**kwargs)
