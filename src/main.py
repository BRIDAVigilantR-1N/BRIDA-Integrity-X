# ==========================================================
# TOOL    : BRIDA-INTEGRITY-X (BI-X)
# AUTHOR  : BRIDA-VigilantR-1N
# ORG     : BRIDACyberForceXploit (West Java, ID)
# VERSION : 1.0.1
# ==========================================================
import psutil
import time

# Daftar hitam perilaku (Binary lokal dilarang akses network)
BLACKLIST = ['ls', 'cat', 'whoami', 'ps', 'grep', 'stat', 'df', 'id']

def start_guard():
    print("="*50)
    print("   BRIDA-INTEGRITY-X v1.0.1 - GUARDING SYSTEM")
    print("   Lead Researcher: BRIDA-VigilantR-1N")
    print("="*50)
    
    try:
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] in BLACKLIST:
                    conns = proc.connections()
                    if conns:
                        for c in conns:
                            if c.status == 'ESTABLISHED':
                                print(f"\033[91m[!] ALERT: {proc.info['name']} (PID:{proc.pid}) detected network activity to {c.raddr.ip}\033[0m")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\n[*] Service Terminated by BRIDA-VigilantR-1N.")

if __name__ == "__main__":
    start_guard()
  
