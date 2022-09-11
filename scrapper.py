import os
import requests
import threading
import time
import remove_duplicates

from colorama import init, Fore

init(autoreset=True)

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

cls()
print(f'''{Fore.RED}
$$$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$\     $$\        $$$$$$\   $$$$$$\  $$$$$$$\   $$$$$$\  $$$$$$$\  $$$$$$$\  $$$$$$$$\ $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |\$$\   $$  |      $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  _____|$$  __$$\ 
$$ |  $$ |$$ |  $$ |$$ /  $$ |\$$\ $$  | \$$\ $$  /       $$ /  \__|$$ /  \__|$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |  $$ |$$ |      $$ |  $$ |
$$$$$$$  |$$$$$$$  |$$ |  $$ | \$$$$  /   \$$$$  /        \$$$$$$\  $$ |      $$$$$$$  |$$$$$$$$ |$$$$$$$  |$$$$$$$  |$$$$$\    $$$$$$$  |
$$  ____/ $$  __$$< $$ |  $$ | $$  $$<     \$$  /          \____$$\ $$ |      $$  __$$< $$  __$$ |$$  ____/ $$  ____/ $$  __|   $$  __$$< 
$$ |      $$ |  $$ |$$ |  $$ |$$  /\$$\     $$ |          $$\   $$ |$$ |  $$\ $$ |  $$ |$$ |  $$ |$$ |      $$ |      $$ |      $$ |  $$ |
$$ |      $$ |  $$ | $$$$$$  |$$ /  $$ |    $$ |          \$$$$$$  |\$$$$$$  |$$ |  $$ |$$ |  $$ |$$ |      $$ |      $$$$$$$$\ $$ |  $$ |
\__|      \__|  \__| \______/ \__|  \__|    \__|           \______/  \______/ \__|  \__|\__|  \__|\__|      \__|      \________|\__|  \__|

{Fore.RED}A Simple Program To Scrape Proxy. (https://github.com/ReCaree/proxy-scrapper)\n''')

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

DEBUG = False

def print_info(t):
  print(f"{Fore.GREEN}[?] {Fore.RED}{t}")

def print_debug(t):
  if (DEBUG == True):
    print(f"{Fore.YELLOW}[*] {t}")

print_info("Scrapping Proxies\n")

if not os.path.isdir("proxy"):
  os.mkdir("proxy")

http = open("proxy/http.txt", "wb")
socks4 = open("proxy/socks4.txt", "wb")
socks5 = open("proxy/socks5.txt", "wb")

def http_worker():
  try:
    time.sleep(0.2)
    print_info("Scrapping HTTP(s) Proxies")
    h = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt")
    h1 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt")
    h2 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all")
    h3 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-https.txt")
    h4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-http.txt")
    h5 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt")
    h6 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt")
    h7 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt")
    h8 = requests.get("https://www.proxy-list.download/api/v1/get?type=http")
    h9 = requests.get("https://www.proxy-list.download/api/v1/get?type=https")
    h10 = requests.get("https://www.proxyscan.io/download?type=http")
    h11 = requests.get("https://www.proxyscan.io/download?type=https")
    h12 = requests.get("https://api.openproxylist.xyz/http.txt")
    h13 = requests.get("http://worm.rip/http.txt")
    h14 = requests.get("https://openproxylist.xyz/http.txt")
    h15 = requests.get("https://proxyspace.pro/http.txt")
    h16 = requests.get("https://proxyspace.pro/https.txt")
    h17 = requests.get("https://rootjazz.com/proxies/proxies.txt")
    print_info("Scrapped HTTP(s) Proxies")

    print_info("Writing HTTP(s) Proxies")
    http.write(h.content)
    http.write(h1.content)
    http.write(h2.content)
    http.write(h3.content)
    http.write(h4.content)
    http.write(h5.content)
    http.write(h6.content)
    http.write(h7.content)
    http.write(h8.content)
    http.write(h9.content)
    http.write(h10.content)
    http.write(h11.content)
    http.write(h12.content)
    http.write(h13.content)
    http.write(h14.content)
    http.write(h15.content)
    http.write(h16.content)
    http.write(h17.content)
    print_info("Wrote HTTP(s) Proxies!\n")
  except Exception as e:
    print_info(f"Failed To Scrap HTTP(s) Proxies: {e}\n")
    exit()

print_debug("Creating HTTP(s) Worker")
th = threading.Thread(target=http_worker)
print_debug("HTTP(s) Worker Created")
print_debug("Starting HTTP(s) Worker")
th.start()
print_debug("HTTP(s) Worker Started\n")

def socks4_worker():
  try:
    time.sleep(0.4)
    print_info("Scrapping SOCKS4 Proxies")
    s4 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt")
    s41 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all")
    s42 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks4.txt")
    s43 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt")
    s44 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt")
    s45 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt")
    s46 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
    s47 = requests.get("https://www.proxyscan.io/download?type=socks4")
    s48 = requests.get("https://api.openproxylist.xyz/socks4.txt")
    s49 = requests.get("https://proxyspace.pro/socks4.txt")
    s410 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
    s411 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
    print_info("Scrapped SOCKS4 Proxies")

    print_info("Writing SOCKS4 Proxies")
    socks4.write(s4.content)
    socks4.write(s41.content)
    socks4.write(s42.content)
    socks4.write(s43.content)
    socks4.write(s44.content)
    socks4.write(s45.content)
    socks4.write(s46.content)
    socks4.write(s47.content)
    socks4.write(s48.content)
    socks4.write(s49.content)
    socks4.write(s410.content)
    socks4.write(s411.content)
    print_info("Wrote SOCKS4 Proxies!\n")
  except Exception as e:
    print_info(f"Failed To Scrap SOCKS4 Proxies: {e}\n")
    exit()

print_debug("Creating SOCKS4 Worker")
ts4 = threading.Thread(target=socks4_worker)
print_debug("SOCKS4 Worker Created")
print_debug("Starting SOCKS4 Worker")
ts4.start()
print_debug("SOCKS4 Worker Started\n")

def socks5_worker():
  try:
    time.sleep(0.6)
    print_info("Scrapping SOCKS5 Proxies")
    s5 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt")
    s51 = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all")
    s52 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt")
    s53 = requests.get("https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt")
    s54 = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/archive/txt/proxies-socks5.txt")
    s55 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt")
    s56 = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
    s57 = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
    s58 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
    s59 = requests.get("https://www.proxyscan.io/download?type=socks5")
    s510 = requests.get("https://api.openproxylist.xyz/socks5.txt")
    s511 = requests.get("https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt")
    s512 = requests.get("https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt")
    s513 = requests.get("http://worm.rip/socks5.txt")
    s514 = requests.get("https://openproxylist.xyz/socks5.txt")
    s515 = requests.get("https://proxyspace.pro/socks5.txt")
    s516 = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
    print_info("Scrapped SOCKS5 Proxies")

    print_info("Writing SOCKS5 Proxies")
    socks5.write(s5.content)
    socks5.write(s51.content)
    socks5.write(s52.content)
    socks5.write(s53.content)
    socks5.write(s54.content)
    socks5.write(s55.content)
    socks5.write(s56.content)
    socks5.write(s57.content)
    socks5.write(s58.content) 
    socks5.write(s59.content)
    socks5.write(s510.content)
    socks5.write(s511.content)
    socks5.write(s512.content)
    socks5.write(s513.content)
    socks5.write(s514.content)
    socks5.write(s515.content)
    socks5.write(s516.content)
    print_info("Wrote SOCKS5 Proxies!\n")
  except Exception as e:
    print_info(f"Failed To Scrap SOCKS5 Proxies: {e}\n")
    exit()

print_debug("Creating SOCKS5 Worker")
ts5 = threading.Thread(target=socks5_worker)
print_debug("SOCKS5 Worker Created")
print_debug("Starting SOCKS5 Worker")
ts5.start()
print_debug("SOCKS5 Worker Started\n")

th.join()
print_debug("HTTP(s) Worker Joined")
ts4.join()
print_debug("SOCKS4 Worker Joined")
ts5.join()
print_debug("SOCKS5 Worker Joined\n")

print_info("Removing Duplicates\n")

print_debug("Creatng HTTP(s) Duplicates Thread")
tdh = threading.Thread(target=remove_duplicates.http_remove_duplicates)
print_debug("HTTP(s) Duplicates Thread Created")
print_debug("Starting HTTP(s) Duplicates Thread")
tdh.start()
print_debug("HTTP(s) Duplicates Thread Started\n")

print_debug("Creatng SOCKS4 Duplicates Thread")
tds4 = threading.Thread(target=remove_duplicates.socks4_remove_duplicates)
print_debug("SOCKS4 Duplicates Thread Created")
print_debug("Starting SOCKS4 Duplicates Thread")
tds4.start()
print_debug("SOCKS4 Duplicates Thread Started\n")

print_debug("Creatng SOCKS5 Duplicates Thread")
tds5 = threading.Thread(target=remove_duplicates.socks5_remove_duplicates)
print_debug("SOCKS5 Duplicates Thread Created")
print_debug("Starting SOCKS5 Duplicates Thread")
tds5.start()
print_debug("SOCKS5 Duplicates Thread Started\n")

tdh.join()
print_debug("HTTP(s) Duplicates Worker Joined")
tds4.join()
print_debug("SOCKS4 Duplicates Worker Joined")
tds5.join()
print_debug("SOCKS5 Duplicates Worker Joined\n")

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")