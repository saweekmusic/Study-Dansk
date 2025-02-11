from fake_useragent import UserAgent

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

UA = UserAgent()