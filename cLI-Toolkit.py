
#!/usr/bin/env python3
# hack_toolkit.py
import argparse
import subprocess
import sys

def cmd_parse(args):
    subprocess.run([sys.executable, 'parse_logs.py', args.file])

def cmd_screenshot(args):
    subprocess.run([sys.executable, 'screenshot_tool.py'])

def cmd_ping(args):
    subprocess.run([sys.executable, 'ping_sweeper.py', args.network])

def cmd_listenkeys(args):
    subprocess.run([sys.executable, 'keyboard_listener_safe.py'])

def main():
    p = argparse.ArgumentParser(prog='hack_toolkit', description='Kleine Sammlung von Lerntools')
    sub = p.add_subparsers(dest='cmd')

    sp = sub.add_parser('parse', help='Logfile parsen')
    sp.add_argument('file')

    ss = sub.add_parser('screenshot', help='Screenshot machen')

    ps = sub.add_parser('ping', help='Subnet pingen')
    ps.add_argument('network')

    ks = sub.add_parser('listenkeys', help='Keyboard-Listener (sichtbar, Lernzweck)')

    args = p.parse_args()
    if args.cmd == 'parse':
        cmd_parse(args)
    elif args.cmd == 'screenshot':
        cmd_screenshot(args)
    elif args.cmd == 'ping':
        cmd_ping(args)
    elif args.cmd == 'listenkeys':
        cmd_listenkeys(args)
    else:
        p.print_help()

if __name__ == '__main__':
    main()
# Ende hack_toolkit.py