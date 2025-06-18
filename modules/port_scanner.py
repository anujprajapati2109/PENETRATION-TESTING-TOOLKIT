import socket

def scan_ports(target, ports):
    print(f"[+] Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            print(f"[OPEN] Port {port}")
            sock.close()
        except:
            pass

def run():
    target = input("Enter target IP or domain: ")
    port_range = input("Enter port range (e.g., 1-100): ")
    start, end = map(int, port_range.split("-"))
    ports = range(start, end + 1)
    scan_ports(target, ports)
