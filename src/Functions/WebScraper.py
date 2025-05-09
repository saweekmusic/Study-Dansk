import random
import time
import requests
from src.Constants import *
from bs4 import BeautifulSoup
import sys

def findURL(search_word: str = None, pos: str = None, url: str = None, proxy = None, header = None):
        # Wait for 3-6 sec
        time.sleep(random.randint(3, 6))

        # Random User-Agent
        if not header:
            header = {'User-Agent': UA.random}

        if not proxy:
            # Random Proxy
            proxy_random = random.choice(PROXIES)
            proxy = {'https': proxy_random, 'http': proxy_random}

        # If url is not empty
        if url:

            # Use it as a sourse
            source = requests.get(url, headers=header, proxies=proxy).text

            # Returning the html code of the requiered word
            soup = BeautifulSoup(source, 'html.parser')
            return soup.find('div', class_='artikel')
        
        # Else
        else:
            # Search for the word
            source = requests.get(f'https://ordnet.dk/ddo/ordbog?query={search_word}', headers=header).text

            # Pulling the html code of the requiered word
            soup = BeautifulSoup(source, 'html.parser')
            article = soup.find('div', class_='artikel')

            # If the word doesn't exist
            if not article:
                print('The word does not exist!')
                sys.exit(1)

            # Check If there is a requested pos
            if not pos:
                return article

            # If the current word does not match the requested pos
            if not EN_TO_DK[pos] not in article.find('span', class_='tekstmedium allow-glossing').text:
                return article
            
            divs = soup.find('div', class_='searchResultBox').find_all('div')

            # Find the required pos of the word in the searchResultBox
            for div in divs:
                if DK_TO_ABBR[EN_TO_DK[pos]] in div.text:
                    return findURL(url=div.find('a')['href'], proxy=proxy, header=header)