from fake_useragent import UserAgent
import requests
import fpdf
from src.Functions.GetProxies import getProxies

# Word Generation Settigns
TOPIC = None            # Topic for word generation, e.g., 'Animals', 'Food', etc.
DU_LEVEL = None         # Danish level, e.g., 'A1', 'A2', etc.
WORDS = []              # List to store generated words

# Part-of-Speech Mappings
EN_TO_DK = {            # English to full Danish POS names
    "noun": "substantiv",
    "verb": "verbum",
    "adjective": "adjektiv"
}

DK_TO_ABBR = {          # Danish POS names to sidebar abbreviations
    "substantiv": "sb.",
    "verbum": "vb.",
    "adjektiv": "adj."
}

POS_TYPES = {           # UI/Display POS types to internal keys
    "Nouns": "noun",
    "Verbs": "verb",
    "Adjectives": "adjective"
}

# Scraping Settings
PROXIES = getProxies()
UA = UserAgent()
