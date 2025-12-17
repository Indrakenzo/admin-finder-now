#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import time
import random
import sys
from datetime import datetime
from colorama import Fore, Style, init

# Inisialisasi warna
init(autoreset=True)

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
]

def simpan_ke_file(pesan):
    # Ini fungsi rahasianya. 'a' artinya append (tambah di bawah), bukan timpa.
    with open("hasil_temuan.txt", "a") as f:
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{waktu}] {pesan}\n")

def cari_pintu_belakang():
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "    ADMIN HUNTER - AUTO SAVE EDITION    ")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

    target_raw = input(Fore.GREEN + "[?] Masukkan Link Target: " + Style.RESET_ALL).strip()
    target = target_raw.replace("http://", "").replace("https://", "").replace("/", "")
    
    nama_file = "link.txt"
    try:
        with open(nama_file, "r") as f:
            paths = f.readlines()
    except FileNotFoundError:
        print(Fore.RED + "\n[!] File 'link.txt' tidak ditemukan!")
        sys.exit()

    print(Fore.BLUE + f"\n[+] Memulai scan... Hasil akan disimpan di 'hasil_temuan.txt'\n")

    for jalur in paths:
        jalur = jalur.strip()
        if not jalur: continue

        url_lengkap = f"http://{target}/{jalur}"
        headers = {'User-Agent': random.choice(user_agents)}

        try:
            response = requests.get(url_lengkap, headers=headers, timeout=5)
            kode = response.status_code

            # LOGIKA UTAMA
            if kode == 200:
                pesan = f"[KETEMU - 200 OK] {url_lengkap}"
                print(Fore.GREEN + pesan)
                simpan_ke_file(pesan) # <--- INI DIA YANG MENYIMPAN
            
            elif kode == 403:
                pesan = f"[DILARANG - 403] {url_lengkap}"
                print(Fore.YELLOW + pesan)
                simpan_ke_file(pesan) # <--- INI JUGA DISIMPAN
            
            elif kode in [301, 302]:
                print(Fore.MAGENTA + f"[REDIRECT - {kode}] {url_lengkap}")
                # Redirect biasanya tidak perlu disimpan, tapi kalau mau, tambah fungsi simpan di sini
            
            else:
                # Kalau 404 atau error lain, cukup print titik biar layar bersih
                print(Fore.RED + ".", end="", flush=True)

        except Exception as e:
            print(Fore.RED + "x", end="", flush=True)

        time.sleep(0.5) 

    print(Fore.CYAN + "\n\n[+] Selesai Bosku. Cek file 'hasil_temuan.txt' untuk lihat hasil.")

if __name__ == "__main__":
    cari_pintu_belakang()
