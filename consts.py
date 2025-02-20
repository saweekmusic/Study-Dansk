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

PROXIES = []
for _ in (range(5)):
    # requests.get('https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all')
    data = requests.get('http://pubproxy.com/api/proxy?https=true&limit=5').json()
    for proxy in data['data']:
        PROXIES.append('https://' + proxy['ipPort'])


UA = UserAgent()