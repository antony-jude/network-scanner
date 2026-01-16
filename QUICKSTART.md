# Quick Start Guide

## Clone on Linux/macOS

```bash
# Clone the repository
git clone <repository-url> network-scanner
cd network-scanner

# Make script executable
chmod +x scanner.py

# Run directly as executable
./scanner.py localhost

# Or run with Python
python3 scanner.py localhost
```

## Installation as System Tool

### Option 1: Direct Usage
```bash
python3 scanner.py <target>
```

### Option 2: Install Package
```bash
# Install in development mode
pip install -e .

# Then use from anywhere
network-scanner <target>
```

### Option 3: Symlink to PATH
```bash
# Create symlink in /usr/local/bin
sudo ln -s $(pwd)/scanner.py /usr/local/bin/network-scanner

# Use from anywhere
network-scanner <target>
```

## Examples

```bash
# Scan localhost
./scanner.py localhost

# Scan specific IP
./scanner.py 192.168.1.100

# Scan domain
./scanner.py example.com
```

## What It Scans

- **FTP** (Port 21)
- **SSH** (Port 22)
- **Telnet** (Port 23)
- **SMTP** (Port 25)
- **DNS** (Port 53)
- **HTTP** (Port 80)
- **POP3** (Port 110)
- **IMAP** (Port 143)
- **HTTPS** (Port 443)
- **MySQL** (Port 3306)
- **RDP** (Port 3389)

## Requirements

- Python 3.6+
- No external dependencies
- Network access to target

## Legal Notice

⚠️ **Only scan systems you own or have explicit written permission to test.**
