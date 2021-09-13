import urllib, urllib.request
import socket


def url_get(url):
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = str(resp.read())
    data = respData.split('\n')
    return data

def addr_write(address):
    with open('./ips.txt', 'a') as file:
        print(address)
        file.write(address+'\n')

def ip_check(url):
    try:
       ip = socket.gethostbyname_ex(url)
       if len(ip) == 3:
            if len(ip[2]) < 2:
                address = ip[2][0]
                addr_write(address)
            else:
                for address in ip[2]:
                    addr_write(address)
    except Exception as e:
        pass

s = '<td align="left" colspan="2">'
networks = []

try:
    url = 'http://netsplit.de/networks'
    data = url_get(url)
    for line in data:
        if s in line:
            lines = line.split('title')
            for _line in lines:
                if 'href' in _line:
                    link1 = _line.split('href=')[1]
                    network_url = 'http://netsplit.de'+link1.replace('"', '')
                    networks.append(network_url)
except Exception as e:
    pass


f = '<a href="/servers/details.php?host=%1$s">'
server_urls = []
for network in networks:    
    try:
        lines = url_get(network)
        for line in lines:
            netdata = line.split(f)
            if len(netdata) > 1:
                server_url = netdata[1].split('</a> ')[0]
                ip_check(server_url)
    except Exception as e:
        pass
   


