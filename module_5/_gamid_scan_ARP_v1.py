import scapy.all as scapy
import argparse

# creating the instance of a class
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', dest='ip_arg', help='Type ip address here')
args = parser.parse_args()
ip = args.ip_arg

arp_req = scapy.ARP()


scapy.arping(ip)

