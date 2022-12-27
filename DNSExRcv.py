import re
import base64
import zlib

class DNSExRcv:
    def __init__(self, **kwargs):
        self.logFile = kwargs.get('filename')
        self.outFile = kwargs.get('outputFile')
        self.domain = kwargs.get('domain')  
        self.verbose = kwargs.get('verbose')
        self.zip = kwargs.get('zip')

    def recoverExfiltrated(self):
        try:
            print("Analysing log file provided...") if self.verbose else None
            with open(self.logFile, "r", encoding="utf8") as log: data = log.read()
            print("Recovering exfiltrated file...") if self.verbose else None
            #File format for Bind9 query log files (if using other DNS server, change the regex accordingly)
            data = re.findall(f"query: (.*)\.{self.domain}", data)
            print("Removing duplicated chunks...") if self.verbose else None
            data = [data[i] for i in range(len(data)) if i == 0 or data[i] != data[i-1]]
            #remove duplicates (could cause problems if the same chunk is sent more than once)
            #data = list(dict.fromkeys(data))
            data = "".join(data)
            print("Decoding recovered file...") if self.verbose else None
            data = base64.b64decode(data)
            if self.zip:
                print("Decompressing recovered file...") if self.verbose else None
                data = zlib.decompress(data)
            print (f"Saving recovered file to {self.outFile}...") if self.verbose else None
            with open(self.outFile, "wb") as out:
                out.write(data) 
        except FileNotFoundError as err:
            print(f"Error reading log file: {err}")
            exit(1)
        except zlib.error as err:
            print(f"Error decompressing recovered file: {err}")
            exit(1)
        except IOError as err:
            print(f"Error in input/output operations when recovering exfiltrated file: {err}")
            exit(1)