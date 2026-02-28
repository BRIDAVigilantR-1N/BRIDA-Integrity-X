# 🛡️ BRIDA-Integrity-X (BI-X) 🇮🇩
**Advanced Behavioral-Based Binary Integrity Monitoring for Linux Infrastructure.**

Developed with passion by **BRIDA-VigilantR-1N** | **BRIDACyberForceXploit**

---

## 🚀 Overview
**BRIDA-Integrity-X (BI-X)** adalah alat keamanan siber yang dirancang untuk mendeteksi ancaman tingkat tinggi seperti *Credential Collectors* dan *Rootkits*. Berbeda dengan metode tradisional yang hanya mengecek `Hash (MD5/SHA)`, BI-X fokus pada **Analisis Perilaku (Behavioral)** secara real-time.

### 🔍 Key Capabilities
| Feature | Description |
| :--- | :--- |
| **Zero-Trust Socket** | Mendeteksi jika binary lokal (ls, cat, whoami) mencoba membuka koneksi internet. |
| **Real-Time Monitoring** | Pemindaian proses aktif secara berkelanjutan dengan penggunaan CPU rendah. |
| **Incident Logging** | Mencatat setiap anomali ke dalam file `incident_report.log` untuk forensik. |
| **Identity Protection** | Melindungi integritas sistem dari binary yang telah dimodifikasi (backdoored). |

---

## 🛠️ Installation & Usage

Pastikan Anda memiliki Python 3 dan library `psutil` terpasang di sistem Linux/Termux Anda.

```bash
# 1. Clone the repository
git clone [https://github.com/BRIDA-VigilantR-1N/BRIDA-Integrity-X.git](https://github.com/BRIDA-VigilantR-1N/BRIDA-Integrity-X.git)

# 2. Enter the directory
cd BRIDA-Integrity-X

# 3. Install dependencies
pip install psutil

# 4. Run the Guard (Require Root for Network Inspection)
sudo python3 src/main.py
```
---

## 📖 Research Documentation
Untuk pemahaman mendalam mengenai metodologi yang saya gunakan, silakan baca dokumen berikut:
* [📄 Technical Whitepaper](docs/WHITEPAPER.md) - Penjelasan Logika & Metodologi.
* [🎬 Usage Demo](docs/DEMO.md) - Skenario simulasi deteksi serangan.

---

## 🤝 Community & Contribution
Saya membangun alat ini untuk memperkuat kedaulatan siber Indonesia. Jika Anda ingin berkontribusi atau melaporkan bug, silakan buka **Issue** atau kirimkan **Pull Request**.

> **"Vigilance is the path to true security."** > — *BRIDA-VigilantR-1N*

---
© 2026 **BRIDACyberForceXploit**. Released under [MIT License](LICENSE).
