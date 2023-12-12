import threading

from colorama import Fore

__LOCK__ = threading.Lock()
DEBUG = True

class Console:  
  @staticmethod
  def print(s: str):
    __LOCK__.acquire()
    print(s)
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
  
  @staticmethod
  def print_info(self, t):
    self.print(f"{Fore.GREEN}[?] {Fore.RED}{t}")
  
  @staticmethod
  def print_debug(self, t):
    if (DEBUG == True):
      self.print(f"{Fore.YELLOW}[*] {t}")

  @staticmethod
  def print_seperator(self):
    self.print(f"{Fore.LIGHTBLACK_EX}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n")