import time, json, threading, requests
from colorama import Fore, init; init(autoreset=True)

__LOCK__ = threading.Lock()
__CONFIG__ = json.load(open("./config.json"))

class Console:
  @staticmethod
  def printf(content: str):
    __LOCK__.acquire()
    print(content
    .replace("+", f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}]{Fore.GREEN}")
    .replace("-", f"{Fore.LIGHTBLACK_EX}[{Fore.RED}+{Fore.LIGHTBLACK_EX}]{Fore.RED}"))
    __LOCK__.release()

  @staticmethod
  def print_logo():
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

class Check(threading.Thread):
  def __init__(self, proxy: str,) -> None:
    self.proxy = proxy

    threading.Thread.__init__(self)
    self.run()

  def run(self):
    p = {'http': self.proxy}
    session = requests.Session()
    res = session.get("https://google.com", proxies=p, timeout=1000)

    if res.status_code == 200:
      with open("./proxy/http-checked.txt", "a", encoding="utf-8") as f:
        f.write(f"{self.proxy}\n")

      Console.printf(f"+ {self.proxy}")
    else:
      Console.printf(f"- {self.proxy}")

Console.print_logo()

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")


for proxy in list(set(open("./proxy/http-removed.txt", "r+", encoding="utf-8").read().splitlines())):
  while threading.active_count() >= __CONFIG__["checker-threads"]:
    time.sleep(0.5)

  try:
    Check(proxy)
  except Exception as e:
    print(e)
    pass