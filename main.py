import os
import random
import time
import concurrent.futures as t
from faker import Faker
from colorama import Fore as F, init
from datetime import datetime, timedelta

init(autoreset=True)

CONFIG = {
    "Author": "Local Tester",
    "Version": "VIU Dummy 1.0",
    "Domain": "example.com",
    "Password": "dummy123",
    "Nomor": "6281234567890",
    "Thread": 5,
    "Proxies": False
}

class ViuDummy:
    def __init__(self):
        self.fake = Faker("id_ID")

    def create_account(self, nomor, use_proxy):
        try:
            print(F.YELLOW + f"[{nomor}] Membuat akun...")

            # Simulasi delay API
            time.sleep(random.uniform(1, 2))

            # Simulasi akun berhasil
            email = self.fake.user_name() + str(random.randint(100,999)) + "@" + CONFIG["Domain"]
            paket = random.choice(["Viu Premium", "Viu Basic", "Viu Trial"])
            exp_date = datetime.now() + timedelta(days=random.randint(3, 30))
            exp_str = exp_date.strftime('%d %B %Y')

            print(F.GREEN + f"Email : {email}\nPaket : {paket}\nExp   : {exp_str}\n")

            with open("accounts_dummy.txt", "a") as f:
                f.write(f"{email}|{paket}|{exp_str}\n")
        except Exception as e:
            print(F.RED + f"[ERROR] {e}")

# Tampilan awal
os.system("cls" if os.name == "nt" else "clear")
print(f'''{F.CYAN}
██████╗ ██╗   ██╗██╗██╗   ██╗
██╔══██╗╚██╗ ██╔╝██║╚██╗ ██╔╝
██████╔╝ ╚████╔╝ ██║ ╚████╔╝ 
██╔═══╝   ╚██╔╝  ██║  ╚██╔╝  
██║        ██║   ██║   ██║   
╚═╝        ╚═╝   ╚═╝   ╚═╝   {F.WHITE}:: Dummy Generator ::
''')

index = ViuDummy()
nomor = CONFIG["Nomor"]

try:
    proxyless = int(input("1. Pakai Proxy (simulasi)\n2. Tanpa Proxy\n\nPilihan: "))
except ValueError:
    print(F.RED + "Masukkan angka 1 atau 2.")
    exit()

print(F.BLUE + "\nSilakan tunggu, akun sedang dibuat...\n")

with t.ThreadPoolExecutor(max_workers=CONFIG['Thread']) as exec:
    futures = [exec.submit(index.create_account, nomor, proxyless) for _ in range(CONFIG['Thread'])]
    t.wait(futures)
