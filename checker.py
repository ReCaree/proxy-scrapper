import time, json, threading, requests
from colorama import Fore, init; init(autoreset=True)

__LOCK__ = threading.Lock()
__CONFIG__ = json.load(open("./config.json"))

class Console:
  @staticmethod
  def printf(content: str):
    __LOCK__.acquire()
    print(content)
    __LOCK__.release()

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
      Console.printf(f"Working: {self.proxy}")

for proxy in list(set(open("./proxy/http-removed.txt", "r+", encoding="utf-8").read().splitlines())):
  while threading.active_count() >= __CONFIG__["checker-threads"]:
    time.sleep(0.5)

  try:
    Check(proxy)
  except Exception as e:
    print(e)
    pass