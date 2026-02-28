# 🛡️ BRIDA-Integrity-X (BI-X) 🇮🇩
**Advanced Behavioral-Based Binary Integrity Monitoring & Active Defense System.**

Developed with passion by **BRIDA-VigilantR-1N** | **BRIDACyberForceXploit**

---

## 🚀 Overview
**BRIDA-Integrity-X (BI-X)** adalah sistem pertahanan aktif yang dirancang untuk mendeteksi dan menghentikan ancaman tingkat tinggi seperti *Credential Collectors* dan *Reverse Shells*. Berbeda dengan metode tradisional, BI-X v1.1.0 kini dilengkapi dengan fitur **Intrusion Prevention System (IPS)** untuk memutus serangan secara otomatis.

### 🔍 Key Capabilities
| Feature | Description |
| :--- | :--- |
| **Zero-Trust Socket** | Mendeteksi jika binary lokal (ls, cat, whoami) mencoba membuka koneksi internet. |
| **Real-Time Monitoring** | Pemindaian proses aktif secara berkelanjutan dengan penggunaan CPU rendah. |
| **Auto-IPS** | **NEW!** Secara otomatis memblokir IP penyerang menggunakan `iptables` saat deteksi anomali. |
| **Incident Logging** | Mencatat setiap upaya eksfiltrasi ke dalam log sistem untuk kebutuhan forensik. |
| **Identity Protection** | Melindungi integritas sistem dari binary yang telah disusupi backdoor. |

---

## 🛠️ Installation & Usage

Pastikan Anda menjalankan alat ini di sistem Linux (Termux/Ubuntu/Debian) dengan akses **Root** agar fitur IPS (iptables) dapat bekerja.

```bash
# 1. Clone the repository
git clone [https://github.com/BRIDA-VigilantR-1N/BRIDA-Integrity-X.git](https://github.com/BRIDA-VigilantR-1N/BRIDA-Integrity-X.git)

# 2. Enter the directory
cd BRIDA-Integrity-X

# 3. Install dependencies
pip install psutil

# 4. Run the Guard in IPS Mode (Requires Root)
sudo python3 src/main.py
```
---

## 📖 Research Documentation
Untuk pemahaman mendalam mengenai metodologi yang saya gunakan, silakan baca dokumen berikut:
Untuk pemahaman mendalam mengenai metodologi yang saya gunakan, silakan baca dokumen berikut:
* 📄 Technical Whitepaper - Penjelasan Logika & Metodologi Riset.
* 🎬 Usage Demo - Skenario simulasi deteksi & pemblokiran IP.

---

## 🤝 Community & Contribution
Saya membangun alat ini sebagai kontribusi untuk memperkuat kedaulatan siber Indonesia. Jika Anda ingin berdiskusi atau memberikan masukan, silakan buka Issue atau kirimkan Pull Request.
"Vigilance is the path to true security. We watch the shadows so you don't have to." > — BRIDA-VigilantR-1N

> **"Vigilance is the path to true security."** > — *BRIDA-VigilantR-1N*

---
© 2026 **BRIDACyberForceXploit**. Released under [MIT License](LICENSE).
