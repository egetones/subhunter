#!/usr/bin/env python3
import requests
import argparse
import sys
from colorama import Fore, Style, init

# Initialize colors
init(autoreset=True)

def scan_subdomains(domain, wordlist_path):
    print(f"\n{Fore.CYAN}[*] Starting SubHunter scan for: {domain}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}[*] Using wordlist: {wordlist_path}{Style.RESET_ALL}")
    print("-" * 50)

    try:
        with open(wordlist_path, 'r') as file:
            # Read all lines
            subdomains = file.read().splitlines()

        for sub in subdomains:
            # Construct the full URL
            url = f"http://{sub}.{domain}"
            
            try:
                # Send a request to the subdomain
                response = requests.get(url, timeout=2)
                
                # If status is 200 (OK), we found a live one!
                if response.status_code == 200:
                    print(f"{Fore.GREEN}[+] Found: {url} (Status: 200){Style.RESET_ALL}")
                else:
                    # Optional: Print other status codes if needed
                    pass
            
            except requests.ConnectionError:
                # Subdomain doesn't exist or is down
                pass
            except KeyboardInterrupt:
                print(f"\n{Fore.RED}[!] Scan interrupted by user.{Style.RESET_ALL}")
                sys.exit()

    except FileNotFoundError:
        print(f"{Fore.RED}[X] Error: Wordlist file '{wordlist_path}' not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[X] Unexpected Error: {e}{Style.RESET_ALL}")

def main():
    parser = argparse.ArgumentParser(description="SubHunter - Simple Subdomain Scanner")
    parser.add_argument("-d", "--domain", required=True, help="Target domain (e.g., google.com)")
    parser.add_argument("-w", "--wordlist", required=True, help="Path to wordlist file")
    
    args = parser.parse_args()
    
    scan_subdomains(args.domain, args.wordlist)

if __name__ == "__main__":
    main()
