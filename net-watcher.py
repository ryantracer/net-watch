import argparse
import os
import subprocess
import scapy.all as scapy
import sys
import pandas as pd
from time import sleep

def scanner(ip_range):

    try:
        arp_request = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')/scapy.ARP(pdst=ip_range)
        ans, un = scapy.srp(arp_request, timeout=2, verbose=0)
    
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
        sleep(1)
        
        c = len(ids-1)

        print('[/] Sending ICMP requests for more hosts [/]')

        param = '-n' if os.name == 'nt' else '-c'

    
        devices = {i: (ip, mac) for i, ip, mac in zip(ids, ips, macs)} 

        return devices
    except Exception as e:
        print(f'[!] Process terminated [!] \n {e}')

def make_device_table(devices):
    df = pd.DataFrame(devices)
    dftrsp = df.transpose()
    dftrsp.columns = ['IP', 'MAC']

    w1, w2 = 20, 20
    print(f"{dftrsp.columns[0]:<{w1}} {dftrsp.columns[1]:<{w2}}")
    print("-" * (w1 + w2 + 2))
    for ip, mac in dftrsp.values:
        print(f"{ip:<{w1}} {mac:<{w2}}")
    

def clean_monitor():
     pass

if __name__ == '__main__':
    devices = scanner('192.168.0.0/24')
    make_device_table(devices)
