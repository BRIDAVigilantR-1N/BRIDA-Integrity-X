# Demo & Penggunaan BRIDA-Integrity-X (BI-X)

### 1. Skenario Serangan (Kasus Credit Collector)
Penyerang mengganti binary `/bin/ls` yang asli dengan binary palsu yang sudah disisipkan *backdoor*. Setiap kali user mengetik `ls`, binary tersebut mengirimkan daftar file ke server penyerang.

### 2. Deteksi oleh BI-X
Saat alat **BI-X** dijalankan oleh **BRIDA-VigilantR-1N**, alat ini akan memantau setiap proses. 

**Output pada Terminal:**
```text
[*] BI-X v1.0.1 - GUARDING SYSTEM
[*] Researcher: BRIDA-VigilantR-1N
--------------------------------------------------
[!] ALERT: ls (PID: 4521) detected network activity to 103.xxx.xxx.xxx
[!] ALERT: whoami (PID: 4522) detected network activity to 103.xxx.xxx.xxx

