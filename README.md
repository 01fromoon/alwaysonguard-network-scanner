# 🛡️ AoA Network Scanner

## 🇬🇧 English

**AoA Network Scanner** is a colorful, interactive, and educational terminal tool for scanning open ports across IP ranges.
✨ **Features:**
- 🎨 Animated and green ASCII art intro
- 🌍 Multi-language support (English & Turkish)
- 🧑‍💻 User-friendly interactive interface, emoji-enhanced prompts
- 🟢 Colorful and clear outputs
- 🛑 Robust input validation (no crashes on bad input)
- 🗃️ Results saved to both the terminal and a timestamped CSV in the `database/` folder
- 🙏 Graceful exit with thank-you message (Ctrl+C friendly)

---

### ▶️ **How to Use**

1. **Install Python 3** (if not already)
2. **Clone or download this repo,** open a terminal in the project folder.
3. **Run:**
   ```
   python AoAnetworkScanner.py
   ```
4. **Follow the emoji-guided prompts:**
   - 🌐 Select language
   - 🖥️ Enter target IP or IP range
   - 🔢 Enter port range
5. **Review results:**  
   - ✅ Open/closed ports are shown in color in your terminal  
   - 📁 Results auto-saved as CSV in `database/`

---

### 💻 **Sample Run**

```
🛡️ AoA Network Scanner | Multi Hacking Tool / By 01fromoon

🌍 1. English
🌍 2. Türkçe
🌐 Select language / Dil seçin (1/2): 1

🖥️ Enter target IP or IP range (e.g. 192.168.1.1-192.168.1.10 or 192.168.1.5): 192.168.1.5
🔢 Enter port range (e.g. 20-80): 22-25

🔎 Scanning 1 IP(s) and 4 port(s)...

✅ [OPEN] 192.168.1.5:22
❌ [CLOSED] 192.168.1.5:23
❌ [CLOSED] 192.168.1.5:24
❌ [CLOSED] 192.168.1.5:25

📁 Scan complete. Results saved to: database/scan_20250527_013000.csv

🙏 Thank you for using, exiting...
```

---

## 🇹🇷 Türkçe

**AoA Network Scanner**; IP aralıklarında port taraması yapan renkli ve eğitsel bir terminal aracıdır.

✨ **Özellikler:**
- 🎨 Animasyonlu ve yeşil ASCII art açılışı
- 🌍 Çoklu dil desteği (İngilizce & Türkçe)
- 🧑‍💻 Kullanıcı dostu, emoji'li arayüz
- 🟢 Renkli ve anlaşılır çıktı
- 🛑 Hatalı girişte çökme yok, uyarı mesajlarıyla yeniden sorar
- 🗃️ Sonuçlar hem terminalde hem de zaman damgalı CSV olarak `database/` klasöründe
- 🙏 Ctrl+C ile çıkışta teşekkür mesajı ve düzgün kapanış

---

### ▶️ **Kullanım**

1. **Python 3 kurulu olsun**
2. **Projeyi indirip bir terminal açın**
3. **Çalıştırın:**
   ```
   python AoAnetworkScanner.py
   ```
4. **Emoji'li yönergeleri takip edin:**
   - 🌍 Dil seçin
   - 🖥️ IP veya IP aralığı girin
   - 🔢 Port aralığı girin
5. **Sonuçlar:**
   - ✅ Açık/Kapalı portlar renkli olarak terminalde görünür  
   - 📁 Sonuçlar otomatik olarak `database/` klasörüne CSV olarak kaydedilir

---

### 💻 **Örnek Çalıştırma**

```
🛡️ AoA Network Scanner | Multi Hacking Tool / By 01fromoon

🌍 1. English
🌍 2. Türkçe
🌐 Select language / Dil seçin (1/2): 2

🖥️ Taranacak IP veya IP aralığı girin (örn: 192.168.1.1-192.168.1.10 ya da 192.168.1.5): 192.168.1.5
🔢 Port aralığı girin (örn: 20-80): 22-25

🔎 1 IP ve 4 port taranıyor...

✅ [AÇIK] 192.168.1.5:22
❌ [KAPALI] 192.168.1.5:23
❌ [KAPALI] 192.168.1.5:24
❌ [KAPALI] 192.168.1.5:25

📁 Taramalar tamamlandı. Sonuçlar: database/scan_20250527_013000.csv dosyasına kaydedildi.

🙏 Kullandığınız için teşekkürler, çıkılıyor...
```

---

**👨‍💻 Author / Yazar:** 01fromoon  
**🎯 Project Type / Proje Türü:** Educational / Eğitsel  
**📝 License / Lisans:** MIT
