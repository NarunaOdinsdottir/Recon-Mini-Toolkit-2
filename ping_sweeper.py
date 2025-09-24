
#!/usr/bin/env python3
# ping_sweeper.py
import subprocess
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed
import ipaddress
import sys

print("Nachtatem breitet seine Schwingen aus und durchforstet das Subnetz mit mächtigen Schlägen...")

def ping(ip, timeout=1000):
    system = platform.system().lower()
    if system == 'windows':
        cmd = ['ping', '-n', '1', '-w', str(timeout), str(ip)]
    else:
        # -c 1 (ein Ping), -W timeout in Sekunden (Linux), macOS uses -W in ms? use -c & -W=1
        cmd = ['ping', '-c', '1', '-W', str(int(max(1, timeout/1000))), str(ip)]
    try:
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return ip, res.returncode == 0
    except Exception:
        return ip, False

def sweep_network(network_cidr, max_workers=100):
    net = ipaddress.ip_network(network_cidr, strict=False)
    ips = [str(ip) for ip in net.hosts()]
    up = []
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(ping, ip): ip for ip in ips}
        for fut in as_completed(futures):
            ip, alive = fut.result()
            if alive:
                up.append(ip)
    return sorted(up)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python ping_sweeper.py 192.168.1.0/24")
        sys.exit(1)
    net = sys.argv[1]
    alive = sweep_network(net)
    print("Erreichbare Hosts:")
    for ip in alive:
        print(" -", ip)
        print(f"Gesamt: {len(alive)} erreichbare Hosts im Subnetz {net}.")
        print(f"Nachtatem hat seine Suche erfolgreich beendet und kehrt in seinen Hort zurück.")
