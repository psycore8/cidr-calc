### CIDR Calculator ###

import sys
import ipaddress

Version = '0.0.1'
spacer = 40
subnet_octets = []

def subnet_calc(ip_address=str, subnet=str):
    network = ipaddress.IPv4Network(f'{ip_address}/{subnet}', strict=False)
    subnet_dec = network.netmask
    subnet_bin = '.'.join(format(int(octet), '08b') for octet in str(subnet_dec).split('.'))
    subnet_inv = ipaddress.IPv4Address(int(subnet_dec) ^ 0xFFFFFFFF)
    subnet_inv_bin = '.'.join(format(int(octet), '08b') for octet in str(subnet_inv).split('.'))
    net_id = network.network_address
    net_bc = network.broadcast_address
    max_hosts = network.num_addresses -2 if network.prefixlen < 31 else network.num_addresses

    return {
        'IP Adress':            ip_address,
        'Subnet (decimal)':     subnet_dec,
        'Subnet (binary)':      subnet_bin,
        'Subnet (inverse)':     subnet_inv,
        'Subnet (inv-bin)':     subnet_inv_bin,
        'Network ID':           net_id,
        'Network Broadcast':    net_bc,
        'Max Hosts':            max_hosts
    }

def main():
    print(f'CIDR Calculator {Version}')
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} 192.168.2.1 255.255.255.0')
        exit()
    net_data = subnet_calc(sys.argv[1], sys.argv[2])
    for key, value in net_data.items():
        print(f'{key}:'.ljust(spacer) + f'{value}')

if __name__ == '__main__':
    main()