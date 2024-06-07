import requests
url = 'https://ip.smartproxy.com/json'
username = 'spxyz7113l'
password = 'Cmu0i4Lotm=um9W6zK'
proxy = f"https://{username}:{password}@gate.smartproxy.com:7000"
result = requests.get(url, proxies = {
    'http': proxy,
    'https': proxy
})
print(result.text)