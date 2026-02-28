# ==========================================================
# TOOL    : BRIDA-INTEGRITY-X (BI-X) - IPS MODE
# AUTHOR  : BRIDA-VigilantR-1N
# VERSION : 1.1.0 (Auto-Block Enabled)
# ==========================================================
import psutil
import time
import os
import subprocess

# Daftar binary kritis yang diawasi (Zero-Trust Policy)
BLACKLIST = ['ls', 'cat', 'whoami', 'ps', 'grep', 'stat', 'df', 'id']

def block_ip(ip_address):
    """Fungsi sakti untuk memblokir IP penyerang via iptables"""
    try:
        # Perintah untuk memblokir IP secara permanen di firewall
        subprocess.run(['sudo', 'iptables', '-A', 'INPUT', '-s', ip_address, '-j', 'DROP'], check=True)
        subprocess.run(['sudo', 'iptables', '-A', 'OUTPUT', '-d', ip_address, '-j', 'DROP'], check=True)
        print(f"\033[93m[🛡️] SYSTEM PROTECTED: IP {ip_address} has been blacklisted.\033[0m")
    except Exception as e:
        print(f"[!] Failed to block IP: {e}")

def run_ips():
    print("="*60)
    print("   BRIDA-INTEGRITY-X v1.1.0 - IPS (INTRUSION PREVENTION)")
    print("   Security Researcher: BRIDA-VigilantR-1N")
    print("="*60)
    
    blocked_cache = [] # Biar nggak blokir IP yang sama berkali-kali

    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] in BLACKLIST:
                    try:
                        conns = proc.connections()
                        for c in conns:
                            if c.status == 'ESTABLISHED':
                                attacker_ip = c.raddr.ip
                                print(f"\033[91m[🚨] HIGH ALERT: {proc.info['name']} (PID:{proc.pid}) connecting to {attacker_ip}\033[0m")
                                
                                if attacker_ip not in blocked_cache:
                                    print(f"[*] Initiating Auto-Block on {attacker_ip}...")
                                    block_ip(attacker_ip)
                                    blocked_cache.append(attacker_ip)
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] IPS Terminated by BRIDA-VigilantR-1N.")

if __name__ == "__main__":
    run_ips()
    
