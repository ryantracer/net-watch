import libs
import clean_sniffing
import make_table
import monitoring
import scanner

parser = libs.argparse.ArgumentParser()
parser.add_argument('-r', '--range', help='ip range you wanna scan for hosts in CIDR notation. (Example: 192.169.0.0/24)')
parser.add_argument('-s', '--sniff', action='store_true' ,help="'sniff the interface you're in")
args = parser.parse_args()

if __name__ == '__main__':
    if args.range:
        print(f'[/] Network range scanner selected [/]')
        devices = scanner.scanner(args.range)
        make_table.make_device_table(devices)
    elif args.sniff:

        iface = None
        bpf_filter = None
        count = None
        timeout = None
        write_pcap = False
        
        try:
            print('[/] Network sniffer selected [/]')
            while True:
                inp = input('[?] Do you wish to setup parameters for the sniffer? [y/n]')
                res = inp.lower()
        
                if res == 'y':
                    pass
                elif res == 'n':
                    break
                else:
                    print('[!] Invalid response [!]')
            clean_sniffing.sniffing(iface=iface,
                                    filter=bpf_filter,
                                    count=count,
                                    timeout=timeout
                                    )
        except Exception as e:
            print(f'[!] {e} [!]')
