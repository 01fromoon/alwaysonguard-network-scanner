import socket
import threading
import csv
import os
from datetime import datetime
import re
import time
import sys

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"
BOLD = "\033[1m"

def animated_ascii_art(lang):
    ascii_lines = [
        "   _____  .__                              ________           ________                       .___",
        "  /  _  \\ |  |__  _  _______  ___.__. _____\\_____  \\   ____  /  _____/ __ _______ _______  __| _/",
        " /  /_\\  \\|  |\\ \\/ \\/ /\\__  \\<   |  |/  ___//   |   \\ /    \\/   \\  ___|  |  \\__  \\\\_  __ \\/ __ | ",
        "/    |    \\  |_\\     /  / __ \\\\___  |\\___ \\/    |    \\   |  \\    \\_\\  \\  |  // __ \\|  | \\/ /_/ | ",
        "\\____|__  /____/\\/\\_/  (____  / ____/____  >_______  /___|  /\\______  /____/(____  /__|  \\____ | ",
        "        \\/                  \\/\\/         \\/        \\/     \\/        \\/           \\/           \\/ ",
        "                                                        Network/Port Scanning Tool / By 01fromoon"
    ]
    for line in ascii_lines:
        for char in line:
            sys.stdout.write(f"{GREEN}{char}{RESET}")
            sys.stdout.flush()
            time.sleep(0.001)
        print()
    if lang == "en":
        print(f"{YELLOW}{BOLD}Welcome! Please follow the instructions below.{RESET}\n")
    else:
        print(f"{YELLOW}{BOLD}Hoşgeldiniz! Lütfen aşağıdaki yönergeleri takip edin.{RESET}\n")

def validate_ip(ip):
    if re.match(r"^\d{1,3}(\.\d{1,3}){3}$", ip):
        return all(0 <= int(part) <= 255 for part in ip.split('.'))
    if '-' in ip:
        try:
            start, end = ip.split('-')
            return validate_ip(start) and validate_ip(end)
        except:
            return False
    return False

def parse_ip_range(ip_range):
    if '-' not in ip_range:
        return [ip_range]
    start_ip, end_ip = ip_range.split('-')
    start_parts = list(map(int, start_ip.split('.')))
    end_parts = list(map(int, end_ip.split('.')))
    ips = []
    for i in range(start_parts[3], end_parts[3] + 1):
        ips.append(f"{start_parts[0]}.{start_parts[1]}.{start_parts[2]}.{i}")
    return ips

def validate_port_range(port_range):
    try:
        port_start, port_end = map(int, port_range.split('-'))
        return 0 < port_start <= port_end <= 65535
    except:
        return False

def scan_port(ip, port, results, lang):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        results.append((ip, port, "OPEN" if lang == "en" else "AÇIK"))
        print(f"{GREEN}[{'OPEN' if lang == 'en' else 'AÇIK'}]{RESET} {CYAN}{ip}:{port}{RESET}")
    except:
        results.append((ip, port, "CLOSED" if lang == "en" else "KAPALI"))
    finally:
        s.close()

def scan_ip_ports(ip, ports, results, lang):
    threads = []
    for port in ports:
        t = threading.Thread(target=scan_port, args=(ip, port, results, lang))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def exit_message(lang):
    msg = f"{YELLOW}{BOLD}Thank you for using, exiting...{RESET}" if lang == "en" else f"{YELLOW}{BOLD}Kullandığınız için teşekkürler, çıkılıyor...{RESET}"
    print(f"\n{msg}")
    time.sleep(2)
    sys.exit(0)

def main():
    lang = "en"  
    try:
        while True:
            print(f"{CYAN}1. English\n2. Türkçe{RESET}")
            lang_input = input(f"{BOLD}Select language / Dil seçin (1/2): {RESET}").strip()
            if lang_input in ("1", "2"):
                lang = "en" if lang_input == "1" else "tr"
                break

        animated_ascii_art(lang)

        while True:
            if lang == "en":
                ip_input = input(f"{YELLOW}Enter target IP or IP range (e.g. 192.168.1.1-192.168.1.10 or 192.168.1.5): {RESET}")
            else:
                ip_input = input(f"{YELLOW}Taranacak IP veya IP aralığı girin (örn: 192.168.1.1-192.168.1.10 ya da 192.168.1.5): {RESET}")
            if all(validate_ip(part.strip()) for part in ip_input.split(',')):
                break
            print(f"{RED}{BOLD}Hatalı giriş! Geçerli bir IP veya IP aralığı giriniz!{RESET}" if lang == "tr" else f"{RED}{BOLD}Invalid IP or IP range! Please try again.{RESET}")

        while True:
            if lang == "en":
                port_input = input(f"{YELLOW}Enter port range (e.g. 20-80): {RESET}")
            else:
                port_input = input(f"{YELLOW}Port aralığı girin (örn: 20-80): {RESET}")
            if validate_port_range(port_input):
                break
            print(f"{RED}{BOLD}Hatalı giriş! Geçerli bir port aralığı giriniz! (örn: 20-80){RESET}" if lang == "tr" else f"{RED}{BOLD}Invalid port range! Please try again.{RESET}")

        ip_list = []
        for part in ip_input.split(','):
            ip_list.extend(parse_ip_range(part.strip()))
        port_start, port_end = map(int, port_input.split('-'))
        ports = list(range(port_start, port_end + 1))
        all_results = []

        print(
            f"{CYAN}{BOLD}Scanning {len(ip_list)} IP(s) and {len(ports)} port(s)...{RESET}" if lang == "en"
            else f"{CYAN}{BOLD}{len(ip_list)} IP ve {len(ports)} port taranıyor...{RESET}")

        for ip in ip_list:
            print(f"\n{BOLD}{ip}{RESET} {('scanning...' if lang == 'en' else 'adresi taranıyor...')}")
            results = []
            scan_ip_ports(ip, ports, results, lang)
            all_results.extend(results)

        os.makedirs("database", exist_ok=True)
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_path = f"database/scan_{now}.csv"
        with open(csv_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["IP", "Port", "Status"] if lang == "en" else ["IP", "Port", "Durum"])
            for row in all_results:
                writer.writerow(row)

        print(
            f"\n{GREEN}{BOLD}Scan complete. Results saved to:{RESET} {csv_path}" if lang == "en"
            else f"\n{GREEN}{BOLD}Taramalar tamamlandı. Sonuçlar:{RESET} {csv_path} {GREEN}dosyasına kaydedildi.{RESET}")

    except KeyboardInterrupt:
        exit_message(lang)
    except Exception as e:
        print(f"{RED}Bir hata oluştu: {e}{RESET}")
        exit_message(lang)

if __name__ == "__main__":
    main()
