from fake_useragent import UserAgent
import requests
import fpdf
from src.Functions.GetProxies import getProxies

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

# For Scraping
PROXIES = getProxies()
UA = UserAgent()

# Info that should be globally available
TOPIC = str
LEVEL = str
TYPES = ['Nouns', 'Verbs', 'Adjectives']

