# ==========================================================
# TOOL    : BRIDA-INTEGRITY-X (BI-X) - IPS MODE
# AUTHOR  : BRIDA-VigilantR-1N
# VERSION : 1.1.0 (Auto-Block Enabled)
# ==========================================================
import psutil
import time
import os

# Daftar yang diawasi ketat
BLACKLIST = ['ls', 'cat', 'whoami', 'sleep', 'id', 'ping']

def run_ips():
    print("="*60)
    print("   BRIDA-INTEGRITY-X v1.1.5 - BEHAVIORAL MODE")
    print("   Researcher: BRIDA-VigilantR-1N")
    print("="*60)
    
    print("[*] Monitoring started... (Press Ctrl+C to stop)")

    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                # CEK 1: Apakah nama proses ada di Blacklist?
                if proc.info['name'] in BLACKLIST:
                    print(f"\033[91m[🚨] ALERT: Unauthorized Process '{proc.info['name']}' Detected! (PID: {proc.pid})\033[0m")
                    
                    # CEK 2: Coba intip koneksi (Behavioral check)
                    try:
                        conns = proc.connections()
                        for c in conns:
                            if c.status == 'ESTABLISHED':
                                print(f"\033[93m[!] BEHAVIOR: Process is sending data to {c.raddr.ip}\033[0m")
                    except:
                        # Di Termux non-root, bagian ini sering skip, tapi ALERT di atas tetep muncul
                        pass
                        
            time.sleep(0.1) # Kecepatan tinggi (10x per detik)
    except KeyboardInterrupt:
        print("\n[*] Stopped by Researcher.")

if __name__ == "__main__":
    run_ips()
    
