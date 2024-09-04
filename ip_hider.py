import requests
import socks
import socket
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import time
from datetime import datetime
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

# Stylish banner with colors
def print_banner():
    banner = f"""
    {Fore.CYAN}╔═════════════════════════════════════════════╗
    {Fore.CYAN}║{Fore.GREEN}           IP Hider Tool                     {Fore.CYAN}║
    {Fore.CYAN}║{Fore.YELLOW}       Coded by Abu Talha                     {Fore.CYAN}║
    {Fore.CYAN}╚═════════════════════════════════════════════╝
    """
    print(banner)
    print(f"{Fore.GREEN}Tool Starting...\n")

# Tor proxy configuration with enhanced security
def create_tor_session():
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    
    # Robust retry configuration for added reliability
    retries = Retry(total=10, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retries)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    return session

# Check IP address through Tor with added anonymity
def check_ip(session):
    try:
        print(f"{Fore.BLUE}[INFO] Checking your IP address through Tor...")
        response = session.get('https://api.ipify.org?format=json')
        response.raise_for_status()
        ip = response.json().get('ip')
        print(f"\n{Fore.GREEN}[SUCCESS] Your IP address (through Tor): {Fore.CYAN}{ip}")
        log_session_details(ip)
    except requests.RequestException as e:
        print(f"{Fore.RED}[ERROR] Request failed: {e}")

# Add stylish separator with colors
def stylish_separator():
    print(f"\n{Fore.MAGENTA}{'='*50}\n")

# Log session details with added timestamp
def log_session_details(ip):
    with open('session_log.txt', 'a') as log_file:
        log_file.write(f"[{datetime.now()}] IP Address: {ip}\n")

# Additional safety measures
def activate_safety():
    print(f"{Fore.YELLOW}[SAFETY] Ensuring all connections go through Tor...\n")
    socks.setdefaultproxy(socks.SOCKS5, "127.0.0.1", 9050)
    socket.socket = socks.socksocket

# Main Function
if __name__ == "__main__":
    activate_safety()
    print_banner()
    session = create_tor_session()
    check_ip(session)
    stylish_separator()
    time.sleep(2)
    print(f"{Fore.GREEN}[INFO] Session completed.\n")
    print(f"{Fore.YELLOW}Thank you for using IP Hider Tool!\n{Style.RESET_ALL}")
