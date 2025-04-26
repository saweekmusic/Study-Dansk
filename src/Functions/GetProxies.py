import requests


# Fetching proxies from 'freeproxydb.com'
def freeproxydb() -> list[str]:
    proxies = []

    # Request proxies
    try:
        data = requests.get('https://freeproxydb.com/api/proxy/search?https=1').json()
        data = data['data']['data']
    except:
        print(f"Can't fetch proxies from freeproxydb.com!")
        return proxies

    # For every given proxy
    for proxy in data:
            
            # Append the proxy to the array
            proxies.append(f'http://{proxy['ip']}:{proxy['port']}')
    
    return proxies


# Fetching proxies from 'pubproxy.com'
def pubproxy() -> list[str]:
    proxies = []

    try:
        for _ in (range(2)):
            data = requests.get('http://pubproxy.com/api/proxy?https=true&limit=5').json()

        # For every given proxy
        for proxy in data['data']:

            # Append the proxy to the array
            proxies.append(f'http://{proxy['ipPort']}')

        return proxies
    except:
        print(f"Can't fetch proxies from pubproxy.com!")
        return proxies



def getProxies() -> list[str]:
    proxies = pubproxy()

    if proxies:
        return proxies
    
    proxies = freeproxydb()
    if proxies:
        return proxies

    return None