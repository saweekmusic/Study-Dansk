from fake_useragent import UserAgent
import requests

# Mapping English determiners to full Danish names
EN_TO_DK = {
    "noun": "substantiv",
    "verb": "verbum",
    "adjective": "adjektiv",
    "adverb": "adverbium"
}

# Mapping full Danish determiners to sidebar abbreviations
DK_TO_ABBR = {
    "substantiv": "sb.",
    "verbum": "vb.",
    "adjektiv": "adj.",
    "adverbium": "adv."
}

# Request proxies
def getProxis() -> list[str]:
    proxies = []

    for _ in (range(2)):
        data = requests.get('http://pubproxy.com/api/proxy?https=true&limit=5').json()

        # For every given proxy
        for proxy in data['data']:
            # Append the proxy to the array
            proxies.append('http://' + proxy['ipPort'])

    return proxies

# An array of available proxies
PROXIES = getProxis()


UA = UserAgent()