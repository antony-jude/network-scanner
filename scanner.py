#!/usr/bin/env python3
import socket
import sys
import time

# -------------------------
# Configuration
# -------------------------

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

VULN_RULES = {
    21: ("FTP detected", "Cleartext authentication possible", "MEDIUM"),
    23: ("Telnet detected", "Unencrypted remote access", "HIGH"),
    25: ("SMTP exposed", "Check for open relay configuration", "MEDIUM"),
    80: ("HTTP detected", "Consider HTTPS enforcement", "LOW"),
    110: ("POP3 detected", "Cleartext email credentials possible", "MEDIUM"),
    3306: ("MySQL exposed", "Database accessible from network", "HIGH"),
    3389: ("RDP exposed", "Remote desktop exposed to network", "HIGH")
}

SOCKET_TIMEOUT = 0.5


# -------------------------
# Network Functions
# -------------------------

def is_host_alive(host):
    """
    Basic liveness check using TCP connection attempt
    """
    try:
        socket.gethostbyname(host)
        return True
    except socket.error:
        return False


def scan_port(host, port):
    """
    Safe TCP connect scan
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(SOCKET_TIMEOUT)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def banner_grab(host, port):
    """
    Attempt to grab service banner (non-intrusive)
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(SOCKET_TIMEOUT)
        sock.connect((host, port))
        try:
            sock.send(b"\r\n")
        except:
            pass
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner if banner else "No banner"
    except Exception:
        return "No banner"


# -------------------------
# Scanning Logic
# -------------------------

def scan_host(host):
    open_ports = {}

    print(f"\n[*] Scanning host: {host}\n")

    for port, service in COMMON_PORTS.items():
        if scan_port(host, port):
            banner = banner_grab(host, port)
            open_ports[port] = {
                "service": service,
                "banner": banner
            }
            print(f"[+] Port {port}/TCP open ({service})")

    return open_ports


def assess_vulnerabilities(open_ports):
    findings = []

    for port in open_ports:
        if port in VULN_RULES:
            findings.append(VULN_RULES[port])

    return findings


# -------------------------
# Reporting
# -------------------------

def print_report(host, open_ports, findings):
    print("\n" + "=" * 50)
    print("NETWORK VULNERABILITY SCAN REPORT")
    print("=" * 50)

    print(f"\nTarget Host: {host}")
    print(f"Scan Time: {time.ctime()}")

    if not open_ports:
        print("\nNo open ports detected.")
    else:
        print("\nOpen Ports & Services:")
        for port, info in open_ports.items():
            print(f" - {port}/TCP ({info['service']})")
            print(f"   Banner: {info['banner']}")

    if findings:
        print("\nSecurity Findings:")
        for title, description, risk in findings:
            print(f" [{risk}] {title} — {description}")
    else:
        print("\nNo high-risk vulnerabilities identified.")

    print("\n⚠️  Disclaimer:")
    print("This scan is for authorized testing only.")
    print("Do NOT scan systems without explicit permission.")
    print("=" * 50 + "\n")


# -------------------------
# Main
# -------------------------

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <target_ip_or_hostname>")
        sys.exit(1)

    target = sys.argv[1]

    try:
        if not is_host_alive(target):
            print("[-] Host appears unreachable or invalid.")
            sys.exit(1)
    except Exception as e:
        print(f"[-] Error resolving host: {e}")
        sys.exit(1)

    open_ports = scan_host(target)
    findings = assess_vulnerabilities(open_ports)
    print_report(target, open_ports, findings)


if __name__ == "__main__":
    main()
