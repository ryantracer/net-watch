import libs
import clean_sniffing
import make_table
import monitoring
import scanner

parser = libs.argparse.ArgumentParser()
parser.add_argument('-r', '--range', help='ip range you wanna scan for hosts in CIDR notation. (Example: 192.169.0.0/24)')
args = parser.parse_args()

if __name__ == '__main__':
    if args.range:
        print(f'[/] Network range scanner selected [/]')
        devices = scanner.scanner(args.range)
        make_table.make_device_table(devices)
