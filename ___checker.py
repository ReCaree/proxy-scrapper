import time, json, multiprocessing, requests, numpy as np
from colorama import Fore, init

from utils import Console; 

init(autoreset=True)

__CONFIG__ = json.load(open("./config.json"))

class CheckHTTP(multiprocessing.Process):
  def __init__(self, proxy: str,) -> None:
    self.proxy = proxy

    multiprocessing.Process.__init__(self)
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

class ProxyChecker():
  def __init__(self, proxyArr) -> None:
    self.checkedProxy = []
    self.proxyArr = proxyArr

    # multiprocessing.Process.__init__(self)
    self.run()

  # Check if proxy is working
  def checkProxy(self,ptype,proxyip):
 
    if ptype == "https":
      proxy = { "https": "https://"+proxyip }
    elif ptype == "http":
      proxy = { "https": "https://"+proxyip }
    elif ptype == "socks5":
      proxy = { "http": "socks5h://"+proxyip, "https": "socks5h://"+proxyip }
    elif ptype == "socks4":
      proxy = { "http": "socks4://"+proxyip, "https": "socks4://"+proxyip } 

    Session = requests.Session()
    response = Session.get('https://google.com', proxies = proxy, timeout=5)
    if response.status_code == 200:
      return ptype
    else:
      return ""

# Validate proxy type
  def verifyProxy(self,proxyArr) -> list: 
    proxy_type = "Invalid"
    # proxy = proxy.replace(" ","")
    # proxy = proxy.replace("\n","")

    checkedProxy = []
    # print("Verifying proxy: {}".format(proxy))

    for val in proxyArr.tolist():
      try:
        proxy_type = self.checkProxy("socks5",val)
      except:
        try:
          proxy_type = self.checkProxy("socks4",val)
        except:
          try:
            proxy_type = self.checkProxy("https",val)
          except:
            try:
              proxy_type = self.checkProxy("http",val)
            except:
              pass   
      if proxy_type != "Invalid":
        print("Proxy {} is valid and it's type is {}".format(val,proxy_type))
        print(proxy_type)
        checkedProxy.append(val)
        self.checkedProxy.append(val)
        print(self.checkedProxy)
      else:
        pass

    return checkedProxy

  def run(self):
    with multiprocessing.Pool() as pool:
        # strVal = str(val)
        result = pool.imap_unordered(self.verifyProxy, self.proxyArr,)

        # print(self.checkedProxy)
        for checkedProxy in result:
          print(checkedProxy)
          self.checkedProxy = checkedProxy
      # for val in np.nditer(self.proxyArr):

Console.print_logo()

print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")

# for proxy in list(set(open("./proxy/http-removed.txt", "r+", encoding="utf-8").read().splitlines())):
  # while threading.active_count() >= __CONFIG__["checker-threads"]:
  #   time.sleep(0.5)

  # try:
  #   Check(proxy)
  # except Exception as e:
  #   print(e)
  #   pass

# print(open("./proxy/http-removed.txt", "r+", encoding="utf-8").read().splitlines())

if __name__ == "__main__":
  httpArray = np.array( open("./proxy/http-test.txt", "r+", encoding="utf-8").read().splitlines())
  
  httpSplitArray = np.array_split(httpArray, multiprocessing.cpu_count())

  for arr in httpSplitArray:
    ProxyChecker(arr).run()
    arr.tolist()

  # for val in np.nditer(arr):
  #   checker.verifyProxy(str(val))

  # checker.join()  