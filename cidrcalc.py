### CIDR Calculator ###

import sys
import ipaddress

Version = '0.0.4'
spacer = 35
subnet_octets = []
args = []

def argument_error():
    print(f'Usage: {sys.argv[0]} IP_ADDRESS / [NETMASK | CIDR]')
    print(f'Usage: {sys.argv[0]} 172.16.1.1/18')
    print(f'Usage: {sys.argv[0]} 192.168.2.1/255.255.255.0')
    exit()

def has_2_arguments(Values=list):
    if len(Values) < 1:
        return True
    else:
        return False
    
def has_valid_arguments(Values=list):
    if len(Values.split('/')) == 2:
        return True
    else:
        return False

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
        'Subnet (inverse)':     subnet_inv,
        'Subnet (binary)':      subnet_bin,
        'Subnet (inv-bin)':     subnet_inv_bin,
        'Network ID':           net_id,
        'Network Broadcast':    net_bc,
        'Max Hosts':            max_hosts
    }

def main():
    print(f'CIDR Calculator {Version}')
    if not has_2_arguments(sys.argv[1]) and not has_valid_arguments(sys.argv[1]):
        argument_error()
    ip_address = sys.argv[1].split('/')[0]
    subnet = sys.argv[1].split('/')[1]
    net_data = subnet_calc(ip_address, subnet)
    for key, value in net_data.items():
        print(f'{key}:'.ljust(spacer) + f'{value}')

if __name__ == '__main__':
    main()