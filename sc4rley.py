import os
import requests
import re
from multiprocessing.dummy import Pool
from colorama import init, Fore
import pystyle
import fake_useragent
import argparse
init()

banner = Rf"""
                  ██████       {Fore.LIGHTWHITE_EX}    _____      __ __       __          
                ██      ██     {Fore.BLUE}   / ___/_____/ // / _____/ /__  __  __
              ██          ██    {Fore.LIGHTWHITE_EX}  \__ \/ ___/ // /_/ ___/ / _ \/ / / /
              ██      ██  ██    {Fore.BLUE} ___/ / /__/__  __/ /  / /  __/ /_/ / 
              ██            ██  {Fore.LIGHTWHITE_EX}/____/\___/  /_/ /_/  /_/\___/\__, /   
                ██      ████     {Fore.BLUE}                            /____/        
  ██              ██  ██                      {Fore.LIGHTWHITE_EX}V1{Fore.RED}.{Fore.LIGHTWHITE_EX}0{Fore.RED}.{Fore.LIGHTWHITE_EX}0   {Fore.RED}[{Fore.LIGHTWHITE_EX}t.me/sc4rleyteam{Fore.RED}]              
██  ██        ████    ██                     Ig: @invisible_turnstile
██    ████████          ██         
  ██              ██      ██    
  ██      ██    ██        ██  {Fore.LIGHTGREEN_EX} - Threaded {Fore.LIGHTWHITE_EX}
    ██      ██████      ██    {Fore.LIGHTRED_EX} - Fake-Headers {Fore.LIGHTWHITE_EX}
      ████          ████      {Fore.LIGHTGREEN_EX} - Big Results {Fore.LIGHTWHITE_EX}
          ██████████            
 
"""
print(pystyle.Colorate.Vertical(pystyle.Colors.red_to_yellow,banner))

HEADERS = {'User-Agent': fake_useragent.UserAgent().random}

SAVE_DIR = "tld_results"

os.makedirs(SAVE_DIR, exist_ok=True)

def tld_cek(tld):
    try:
        page = 1
        while True:
            url = f'http://pluginu.com/domain-zone/{tld}/{page}'
            response = requests.get(url, headers=HEADERS)
            if response.status_code != 200:
                print(f"{Fore.RED}Error: {url} is down.")
                break

            domains = re.findall(r'<button class="btn btn-default pull-left" type="button">\n  (.*?)</button></a>', response.text)
            if not domains:
                print(f"{Fore.CYAN}TLD not found: [{tld}]")
                break

            
            print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Page => {Fore.YELLOW}{page}{Fore.WHITE} | TLD =>{Fore.BLUE} {tld}{Fore.WHITE} | Domains =>{Fore.YELLOW} {len(domains)}")
            for site in domains:

                print(f"{Fore.WHITE}[{Fore.BLUE}+{Fore.WHITE}] Page => {Fore.YELLOW}{page}{Fore.WHITE} | TLD =>{Fore.BLUE} {tld}{Fore.WHITE} | Domain =>{Fore.YELLOW} {site}")
            kayit = os.path.join(SAVE_DIR, f'tld_grabbed_{tld}.txt')
            with open(kayit, 'a') as file:
                file.writelines([f"http://{domain}\n" for domain in domains])

            page += 1
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="SC4RLEY - TLD Grabber")
    parser.add_argument("-t", "--tld", required=True, help="Target TLD to scan")
    args = parser.parse_args()

    tld = args.tld.strip()
    if not tld:
        print(f"{Fore.RED}Error: TLD is null.")
        return

    try:
        with Pool(5) as pool:
            pool.map(tld_cek, [tld])
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

if __name__ == "__main__":
    main()
