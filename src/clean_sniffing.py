import libs

def clean_sniffing():
    pass
def packet_tracer(packet):
    if libs.scapy.IP in packet:
        print(f'From {packet[libs.scapy.IP].src} to {packet[libs.scapy.IP].dst}')

def sniffing(iface=None, filter=None, count=None, timeout=None):
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
