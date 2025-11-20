<div align="center">

# SubHunter

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Type](https://img.shields.io/badge/Type-Reconnaissance-red)

<p>
  <strong>A lightweight subdomain scanner for penetration testing and bug bounty hunting.</strong>
</p>

[Report Bug](https://github.com/your-username/subhunter/issues) · [Request Feature](https://github.com/your-username/subhunter/issues)

</div>

---

## Description

**SubHunter** is a Python-based CLI tool designed for **Reconnaissance (Recon)**. It helps security researchers and system administrators discover active subdomains of a target website.

It works by utilizing a "Wordlist" to brute-force potential subdomains (e.g., `admin.target.com`, `dev.target.com`) and checks for valid HTTP responses. Finding hidden subdomains is often the first step in mapping an attack surface.

### Key Features

  * Fast Discovery:** Quickly checks valid subdomains using HTTP requests.
  * Color Coded:** Clear, colorized terminal output for easy reading.
  * Wordlist Support:** Works with any custom text-based wordlist.
  * Error Handling:** Gracefully handles connection errors and timeouts.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/subhunter.git](https://github.com/your-username/subhunter.git)
   cd subhunter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the tool by providing a target domain and a wordlist.

**Basic Command:**
```bash
python3 subhunter.py -d target.com -w subdomains.txt
```

**Sample Output:**
```text
[*] Starting SubHunter scan for: google.com
[*] Using wordlist: subdomains.txt
--------------------------------------------------
[+] Found: [http://www.google.com](http://www.google.com) (Status: 200)
[+] Found: [http://mail.google.com](http://mail.google.com) (Status: 200)
[+] Found: [http://blog.google.com](http://blog.google.com) (Status: 200)
```

---

## ⚠️ Disclaimer

This tool is developed for **educational purposes and authorized security testing only**.
Using this tool against targets without prior mutual consent is illegal. The developer is not responsible for any misuse or damage caused by this program.

---

## License

Distributed under the MIT License. See `LICENSE` for more information.
