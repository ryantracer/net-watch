import libs

def scanner(ip_range):
    try:
        arp_request = libs.scapy.Ether(dst='ff:ff:ff:ff:ff:ff')/libs.scapy.ARP(pdst=ip_range)
        ans, un = libs.scapy.srp(arp_request, timeout=2, verbose=0)
    
        print('[/] Scanning through ARP [/]')

        if ans:
            ips = []
            macs = []
            ids = []
            c = 0
            for sent, recv in ans:
                ips.append(recv.psrc)
                macs.append(recv.hwsrc)
                ids.append(f'{c}')
                c += 1
        libs.sleep(1)
        
        c = len(ids)-1

        param = '-n' if libs.os.name == 'nt' else '-c'
    
        devices = {i: (ip, mac) for i, ip, mac in zip(ids, ips, macs)} 

        return devices
    except Exception as e:
        print(f'[!] Process terminated [!] \n {e}')

