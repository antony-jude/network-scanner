# Network Scanner

A lightweight Python network vulnerability scanner for authorized security testing. Detects open ports and identifies potential security vulnerabilities on target systems.

## Features

- **Port Scanning**: Scans common ports (FTP, SSH, HTTP, HTTPS, MySQL, RDP, etc.)
- **Service Detection**: Identifies services running on open ports
- **Banner Grabbing**: Attempts to retrieve service banners for version detection
- **Vulnerability Assessment**: Flags common security issues and risk levels
- **Clean Reporting**: Generates formatted vulnerability reports

## Requirements

- Python 3.6+
- Linux/macOS/Windows with network access
- No external dependencies (uses only Python standard library)

## Installation

### Clone the Repository
```bash
git clone https://github.com/antony-jude/network-scanner.git
cd network-scanner
```

### Make Script Executable (Linux/macOS)
```bash
chmod +x scanner.py
```

## Usage

### Basic Scan
```bash
python3 scanner.py <target_ip_or_hostname>
```

### Examples
```bash
# Scan localhost
python3 scanner.py localhost

# Scan a specific IP
python3 scanner.py 192.168.1.1

# Scan a hostname
python3 scanner.py example.com
```

## Output

The scanner produces a formatted report showing:
- **Target Host**: IP or hostname scanned
- **Open Ports**: Detected open ports with service names
- **Banners**: Service version information (if available)
- **Security Findings**: Identified vulnerabilities with risk levels

### Risk Levels
- **HIGH**: Critical security issues (e.g., database exposed, RDP accessible)
- **MEDIUM**: Moderate concerns (e.g., unencrypted services)
- **LOW**: Informational findings (e.g., HTTP detected)

## Example Output

```
==================================================
NETWORK VULNERABILITY SCAN REPORT
==================================================

Target Host: localhost
Scan Time: Thu Jan 16 13:12:40 2026

Open Ports & Services:
 - 3306/TCP (MySQL)
   Banner: 8.0.43

Security Findings:
 [HIGH] MySQL exposed — Database accessible from network

⚠️  Disclaimer:
This scan is for authorized testing only.
Do NOT scan systems without explicit permission.
==================================================
```

## Legal & Ethical Notice

**IMPORTANT**: This tool is designed for authorized security testing only. 

- ✅ **Allowed**: Testing systems you own or have explicit permission to test
- ❌ **NOT Allowed**: Unauthorized scanning of systems you don't own
- ❌ **NOT Allowed**: Using this tool for malicious purposes

Unauthorized network scanning may violate laws in your jurisdiction. Ensure you have written permission before scanning any system.

## Technical Details

### Scanned Ports

| Port | Service | Risk |
|------|---------|------|
| 21   | FTP     | MEDIUM |
| 22   | SSH     | - |
| 23   | Telnet  | HIGH |
| 25   | SMTP    | MEDIUM |
| 53   | DNS     | - |
| 80   | HTTP    | LOW |
| 110  | POP3    | MEDIUM |
| 143  | IMAP    | - |
| 443  | HTTPS   | - |
| 3306 | MySQL   | HIGH |
| 3389 | RDP     | HIGH |

### How It Works

1. **Host Liveness Check**: Verifies the target host is reachable
2. **Port Scanning**: Attempts TCP connections to common ports
3. **Service Identification**: Maps open ports to known services
4. **Banner Grabbing**: Retrieves service information without intrusion
5. **Vulnerability Assessment**: Evaluates security implications
6. **Reporting**: Generates human-readable scan report

## Performance Notes

- Default socket timeout: 0.5 seconds
- Scan typically completes in 5-10 seconds for all 11 ports
- Timeout can be adjusted by modifying `SOCKET_TIMEOUT` in the script

## Contributing

Contributions are welcome! Please:
1. Test thoroughly before submitting
2. Follow existing code style
3. Add comments for any new functionality
4. Ensure compatibility with Python 3.6+

## License

This project is provided as-is for educational and authorized security testing purposes.

## Disclaimer

Users are solely responsible for complying with all applicable laws and regulations. The authors assume no liability for misuse of this tool.
