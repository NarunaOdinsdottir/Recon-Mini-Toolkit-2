#!/usr/bin/env python3
# parse_logs.py
import re
import csv
import sys
from pathlib import Path

IP_RE = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
ERROR_KEYWORDS = ['error', 'fail', 'exception', 'critical', 'fatal']  # erweiterbar

print("Nachtatem erhebt seinen Blick und durchforstet die Logdatei...")
def parse_log(path):
    ips = set()
    error_lines = []
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        for lineno, line in enumerate(f, start=1):
            lcase = line.lower()
            found_ips = IP_RE.findall(line)
            for ip in found_ips:
                # einfache Validierung 0-255
                if all(0 <= int(p) <= 255 for p in ip.split('.')):
                    ips.add(ip)
            if any(k in lcase for k in ERROR_KEYWORDS):
                error_lines.append((lineno, line.rstrip('\n')))
    return ips, error_lines

def save_csv(ips, errors, out_prefix='parsed'):
    Path('out').mkdir(exist_ok=True)
    with open(f'out/{out_prefix}_ips.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['ip'])
        for ip in sorted(ips):
            writer.writerow([ip])
    with open(f'out/{out_prefix}_errors.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['lineno', 'line'])
        for lineno, line in errors:
            writer.writerow([lineno, line])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python parse_logs.py /pfad/zur/logdatei.log")
        sys.exit(1)
    path = sys.argv[1]
    ips, errors = parse_log(path)
    print(f"Mein Drachenblick hat folgende IPs gefunden: {len(ips)}")
    print(f"Fehlerzeilen: {len(errors)}")
    save_csv(ips, errors)
    print("Die Ergebnisse liegen in meinem Hort in ./out/ gespeichert.")
