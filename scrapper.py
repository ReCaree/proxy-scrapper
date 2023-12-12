import os
import requests
import threading
import time

from __checker import *
from remove_duplicates import *
from colorama import init, Fore
from utils import Console

__LOCK__ = threading.Lock()

init(autoreset=True)

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

cls()

Console.print_logo()

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

Console.print("Scrapping Proxies\n")

if not os.path.isdir("proxy"):
  os.mkdir("proxy")

http = open("proxy/http.txt", "wb")
socks4 = open("proxy/socks4.txt", "wb")
socks5 = open("proxy/socks5.txt", "wb")

def http_worker():
  try:
    time.sleep(0.2)
    Console.print("Scrapping HTTP(s) Proxies")
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
    Console.print("Scrapped HTTP(s) Proxies")

    Console.print("Writing HTTP(s) Proxies")
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
    Console.print("Wrote HTTP(s) Proxies!\n")
  except Exception as e:
    Console.print(f"Failed To Scrap HTTP(s) Proxies: {e}\n")
    exit()

Console.print("Creating HTTP(s) Worker")
th = threading.Thread(target=http_worker)
Console.print("HTTP(s) Worker Created")
Console.print("Starting HTTP(s) Worker")
th.start()
Console.print("HTTP(s) Worker Started\n")

def socks4_worker():
  try:
    time.sleep(0.4)
    Console.print("Scrapping SOCKS4 Proxies")
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
    Console.print("Scrapped SOCKS4 Proxies")

    Console.print("Writing SOCKS4 Proxies")
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
    Console.print("Wrote SOCKS4 Proxies!\n")
  except Exception as e:
    Console.print(f"Failed To Scrap SOCKS4 Proxies: {e}\n")
    exit()

Console.print("Creating SOCKS4 Worker")
ts4 = threading.Thread(target=socks4_worker)
Console.print("SOCKS4 Worker Created")
Console.print("Starting SOCKS4 Worker")
ts4.start()
Console.print("SOCKS4 Worker Started\n")

def socks5_worker():
  try:
    time.sleep(0.6)
    Console.print("Scrapping SOCKS5 Proxies")
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
    Console.print("Scrapped SOCKS5 Proxies")

    Console.print("Writing SOCKS5 Proxies")
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
    Console.print("Wrote SOCKS5 Proxies!\n")
  except Exception as e:
    Console.print(f"Failed To Scrap SOCKS5 Proxies: {e}\n")
    exit()

Console.print("Creating SOCKS5 Worker")
ts5 = threading.Thread(target=socks5_worker)
Console.print("SOCKS5 Worker Created")
Console.print("Starting SOCKS5 Worker")
ts5.start()
Console.print("SOCKS5 Worker Started\n")

th.join()
Console.print("HTTP(s) Worker Joined")
ts4.join()
Console.print("SOCKS4 Worker Joined")
ts5.join()
Console.print("SOCKS5 Worker Joined\n")

Console.print("Removing Duplicates\n")

Console.print("Creating HTTP(s) Duplicates Thread")
tdh = threading.Thread(target=http_remove_duplicates)
Console.print("HTTP(s) Duplicates Thread Created")
Console.print("Starting HTTP(s) Duplicates Thread")
tdh.start()
Console.print("HTTP(s) Duplicates Thread Started\n")

Console.print("Creating SOCKS4 Duplicates Thread")
tds4 = threading.Thread(target=socks4_remove_duplicates)
Console.print("SOCKS4 Duplicates Thread Created")
Console.print("Starting SOCKS4 Duplicates Thread")
tds4.start()
Console.print("SOCKS4 Duplicates Thread Started\n")

Console.print("Creating SOCKS5 Duplicates Thread")
tds5 = threading.Thread(target=socks5_remove_duplicates)
Console.print("SOCKS5 Duplicates Thread Created")
Console.print("Starting SOCKS5 Duplicates Thread")
tds5.start()
Console.print("SOCKS5 Duplicates Thread Started\n")

tdh.join()
Console.print("HTTP(s) Duplicates Worker Joined")
tds4.join()
Console.print("SOCKS4 Duplicates Worker Joined")
tds5.join()
Console.print("SOCKS5 Duplicates Worker Joined\n")

# Console.print("Checking Proxies\n")

# def check_proxy(file, file2):
#   checker = ProxyChecker()
#   checker.checkList(file, file2)

# Console.print("Creating HTTP(s) Checker Thread")
# tch = threading.Thread(target=check_proxy, args=("./proxy/http-removed.txt", "./proxy/http-checked", ))
# Console.print("HTTP(s) Checker Thread Created")
# Console.print("Starting HTTP(s) Checker Thread")
# tch.start()
# Console.print("HTTP(s) Checker Thread Started\n")

# Console.print("Creating SOCKS4 Checker Thread")
# tcs4 = threading.Thread(target=check_proxy, args=("./proxy/socks4-removed.txt", "./proxy/socks4-checked", ))
# Console.print("SOCKS4 Checker Thread Created")
# Console.print("Starting SOCKS4 Checker Thread")
# tcs4.start()
# Console.print("SOCKS4 Checker Thread Started\n")

# Console.print("Creating SOCKS5 Checker Thread")
# tcs5 = threading.Thread(target=check_proxy, args=("./proxy/socks5-removed.txt", "./proxy/socks5-checked", ))
# Console.print("SOCKS5 Checker Thread Created")
# Console.print("Starting SOCKS5 Checker Thread")
# tcs5.start()
# Console.print("SOCKS5 Checker Thread Started\n")

# tch.join()
# Console.print("HTTP(s) Checker Worker Joined")
# tcs4.join()
# Console.print("SOCKS4 Checker Worker Joined")
# tcs5.join()
# Console.print("SOCKS5 Checker Worker Joined\n")

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")