import socket
import subprocess
import sys
from datetime import datetime
import os


def get_ip_address(target):
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid hostname or IP address")
        sys.exit()
    return ip_address


def port_scan(ip_address):
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        result = s.connect_ex((ip_address, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()


def get_connected_hosts():
    command = "arp -a"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
    output = process.communicate()[0]
    output = output.decode("utf-8")
    lines = output.split("\n")
    hosts = []
    for line in lines:
        if "interface" in line.lower():
            continue
        if "incomplete" in line.lower():
            continue
        if len(line.strip()) == 0:
            continue
        parts = line.split()
        ip_address = parts[0]
        mac_address = parts[1]
        hosts.append({"ip_address": ip_address, "mac_address": mac_address})
    return hosts


if __name__ == "__main__":
    target = input("Enter the target IP address or domain name: ")
    ip_address = get_ip_address(target)
    print("-" * 60)
    print("Connected hosts:")
    print("-" * 60)
    hosts = get_connected_hosts()
    for host in hosts:
        print(f"IP address: {host['ip_address']}, MAC address: {host['mac_address']}")

    print("-" * 60)
    print(f"Scanning target {target} ({ip_address})")
    print("-" * 60)
    start_time = datetime.now()
    port_scan(ip_address)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Scan completed in {total_time}")
    print("-" * 60)







#mid-evaluation : IP, UI
#final-evaluation : IP, MAC, verify, UI
#---------------------PHASE2(includes table thingy)---------------------#
# import socket
# import subprocess
# import sys
# from datetime import datetime
# import os


# def get_ip_address(target):
#     try:
#         ip_address = socket.gethostbyname(target)
#     except socket.gaierror:
#         print("Invalid hostname or IP address")
#         sys.exit()
#     return ip_address


# def port_scan(ip_address):
#     for port in range(1, 65536):
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.settimeout(0.1)
#         result = s.connect_ex((ip_address, port))
#         if result == 0:
#             print(f"Port {port} is open")
#         s.close()


# def get_connected_hosts():
#     command = "arp -a"
#     process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
#     output = process.communicate()[0]
#     output = output.decode("utf-8")
#     lines = output.split("\n")
#     hosts = []
#     for line in lines:
#         if "interface" in line.lower():
#             continue
#         if "incomplete" in line.lower():
#             continue
#         if len(line.strip()) == 0:
#             continue
#         parts = line.split()
#         ip_address = parts[0]
#         mac_address = parts[1]
#         hosts.append({"ip_address": ip_address, "mac_address": mac_address})
#     return hosts


# def classify_suspicious_hosts(hosts, suspicious_macs):
#     suspicious_hosts = []
#     for host in hosts:
#         if host["mac_address"] in suspicious_macs:
#             suspicious_hosts.append(host)
#     return suspicious_hosts


# if __name__ == "__main__":
#     target = input("Enter the target IP address or domain name: ")
#     ip_address = get_ip_address(target)
#     print("-" * 60)
#     print(f"Scanning target {target} ({ip_address})")
#     print("-" * 60)
#     start_time = datetime.now()
#     port_scan(ip_address)
#     end_time = datetime.now()
#     total_time = end_time - start_time
#     print(f"Scan completed in {total_time}")
#     print("-" * 60)
#     print("Connected hosts:")
#     hosts = get_connected_hosts()
#     for host in hosts:
#         print(f"IP address: {host['ip_address']}, MAC address: {host['mac_address']}")
#     print("-" * 60)
#     print("Suspicious hosts:")
#     suspicious_macs = ["00:11:22:33:44:55", "AA:BB:CC:DD:EE:FF"] # example list of suspicious MAC addresses
#     suspicious_hosts = classify_suspicious_hosts(hosts, suspicious_macs)
#     for host in suspicious_hosts:
#         print(f"IP address: {host['ip_address']}, MAC address: {host['mac_address']}")
