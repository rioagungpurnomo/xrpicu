#!/usr/bin/python3
try:
  from requests.exceptions import RequestException
  from rich.console import Console
  import requests, time, os, json
  from rich.panel import Panel
  from rich import print
  from random import choice
  from fake_useragent import UserAgent
  from bs4 import BeautifulSoup
except (Exception) as e:
  exit(f"[Error]{str(e).capitalize()}!")
 
proxy = []
user_agent = UserAgent().random
 
class Xrpicu:
  def __init__(self) -> None:
    pass
  
  def logo(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    getIp = requests.get("https://api.myip.com").json()
    ip = getIp["ip"]
    print(Panel(f"""[bold red]●[bold yellow] ●[bold green] ●[/]
[bold white]
      __  ______  ____  _            
      \ \/ /  _ \|  _ \(_) ___ _   _ 
       \  /| |_) | |_) | |/ __| | | |
       /  \|  _ <|  __/| | (__| |_| |
      /_/\_\_| \_\_|   |_|\___|\__,_|

          [italic white on red]You IP : {ip}""", style="bold bright_black", width=56))
  
  def getproxy(self):
    with open('proxy.json') as prohtttp:
      datahttp = json.load(prohtttp)
    for dhttp in datahttp:
      proxies_response = requests.get(dhttp)
      proxies = proxies_response.text.split('\n')
      proxies = [proxy.strip() for proxy in proxies if proxy.strip()]
      for ddh in proxies:
        proxy.append(ddh)
    print("[bold bright_black]   ╰─>[bold green] Proxy updated successfully!", end='\r')
    time.sleep(3)

  def proxy(self):
    proxies = {
      "http": "http://" + choice(proxy).replace('http://', '')
    }
    return proxies
    
  def pay(self, session, username, token, wallet):
      session.headers.update({
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': f'Bearer {token}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Host': 'xrp.icu',
        'Origin': 'https://xrp.icu',
        'Referer': 'https://xrp.icu/spin',
        'User-Agent': user_agent
      })
      response = session.get("https://xrp.icu/admin-api/system/account-balances/get", proxies=self.proxy())
      user = response.json()["data"]
      session.headers.update({
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': f'Bearer {token}',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Host': 'xrp.icu',
        'Origin': 'https://xrp.icu',
        'Referer': 'https://xrp.icu/withdraw',
        'User-Agent': user_agent
      })
      response2 = session.get("https://xrp.icu/admin-api/system/auto-pay/get", proxies=self.proxy())
      response3 = session.post("https://xrp.icu/admin-api/system/account/pay", json=json.dumps({
        "currency": "usd",
        "address": wallet["address"],
        "tag": int(wallet["memo"]),
        "name": "XRP"
      }), proxies=self.proxy())

      response2 = response2.json()
      response3 = response3.json()
      print(user)
      print(response2)
      print(response3)
      exit()
  
  def login(self):
    with open('accounts.json') as json_file:
      data = json.load(json_file)
        
    for account in data:
      username = account['username']
      session = requests.Session()
      session.headers.update({
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Host': 'xrp.icu',
        'Origin': 'https://xrp.icu',
        'Referer': 'https://xrp.icu/login',
        'User-Agent': user_agent
      })
      response = session.post("https://xrp.icu/admin-api/system/auth/login", json={
        "username": username,
        "password": account["password"]
      }, proxies=self.proxy())
      response = response.json()
      if (response["code"] == 0):
        pay = self.pay(session, username, response["data"]["accessToken"], account["wallet"])
      else:
        print(Panel(f"[italic red]Please set the accounts.json file first!", style="bold bright_black", width=56, title=">>> Error <<<"))
        
  def run(self):
    try:
      print(Panel(f"[italic white]You can stop the process at any time by pressing CTRL + Z keys.[/]", style="bold bright_black", width=56, title=">>> Note <<<"))
      try:
        self.login()
      except (RequestException):
        print("[bold bright_black]   ╰─>[bold red] No internet!", end='\r')
        time.sleep(10.5)
        self.login()
      except (KeyboardInterrupt):
        print("                                                       ", end='\r')
        time.sleep(2.5)
        self.login()
    except (Exception) as e:
      print(Panel(f"[italic red]{str(e).capitalize()}!", style="bold bright_black", width=56, title=">>> Error <<<"))
      exit()
  

if __name__ == '__main__':
  try:
    Xrpicu().logo()
    print(Panel(f"[italic blue]Currently updating proxy, please wait...", style="bold bright_black", width=56, title=">>> Update Proxy <<<"))
    Xrpicu().getproxy()
    Xrpicu().logo()
    Xrpicu().run()
  except (KeyboardInterrupt, KeyboardInterrupt):
    exit()