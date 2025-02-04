# Local Classes
from exampleclass import Meaning
from expressionsclass import Expression

# Import libreries
import requests
from bs4 import BeautifulSoup
from translatefunc import * 

# Mapping English POS to full Danish names
EN_TO_DK = {
    "noun": "substantiv",
    "verb": "verbum",
    "adjective": "adjektiv",
    "adverb": "adverbium"
}

# Mapping full Danish POS to sidebar abbreviations
DK_TO_ABBR = {
    "substantiv": "sb.",
    "verbum": "vb.",
    "adjektiv": "adj.",
    "adverbium": "adv."
}

class Word:
    # MARK: Attributes
    word: str = None
    pos: str = None
    gender: str = None
    bending: list[str] = []
    pronunciation: str = None
    meanings: list[Meaning] = []

    # TODO: Implement Expressions
    # expressions: list[Expression] = []


    # MARK: Init definition
    def __init__(self, search_word: str = None, pos: str = None, url: str = None):

        # If url is not empty
        if url:

            # Use it as a sourse
            source = requests.get(url).text

            # Pulling the html code of the requiered word
            soup = BeautifulSoup(source, 'html.parser')
            article = soup.find('div', class_='artikel')
        
        # Else
        else:
            source = requests.get(f'https://ordnet.dk/ddo/ordbog?query={search_word}').text

            # Pulling the html code of the requiered word
            soup = BeautifulSoup(source, 'html.parser')
            article = soup.find('div', class_='artikel')

            # If the word doesn't exist
            if not article:
                return None

            if pos:
                if EN_TO_DK[pos] not in article.find('span', class_='tekstmedium allow-glossing').text:
                    divs = soup.find('div', class_='searchResultBox').find_all('div')

                    for div in divs:
                        if DK_TO_ABBR[EN_TO_DK[pos]] in div.text:
                            return self.__init__(url=div.find('a')['href'])

        # Assigning Word
        self.word = self.word_procc(article)

        # Assigning POS
        self.pos = self.pos_procc(article, 0)

        # Assigning Gender
        self.gender = self.gender_procc(article)

        # Assigning Bending
        self.bending_procc(article)

        # Assigning Pronunciation
        self.pronunciation = self.pronun_procc(article)

        # Assigning Meanings
        self.meaning_procc(article)


    # MARK: Word def
    def word_procc(self, article):
        # Find word in the source html
        word = article.find('span', class_='match')

        # If the 'word' has a number after it
        if word.find('span', class_='super'):

            # Remove it from the scope
            word.find('span', class_='super').decompose()

        return word.text

    
    # MARK: POS def
    def pos_procc(self, article, index):

        if index > 1:
            return None
            
        word_info = article.find('span', class_='tekstmedium allow-glossing').text
        word_info = word_info.split(', ')

        return word_info[index]


    # MARK: Gender def
    def gender_procc(self, article):
        # If it is a noun
        if self.pos == 'substantiv':
            # And if it is the et-word
            if self.pos_procc(article, 1) == 'intetkøn':
                # Assign et
                return 'et'
            # Else if it is the en-word
            else:
                # Assign en
                return 'en'
        # Else if it is a verb
        elif self.pos == 'verbum':
            # Assign at
            return 'at'
    

    # MARK: Bending def
    def bending_procc(self, article):
        # Get benfing section from the site
        bending_section = article.find('div', id='id-boj')

        # Find the bending themselves from the section and break them into an array
        bending_section = bending_section.find('span', class_='tekstmedium allow-glossing').text.strip().split(', ')

        # For every bending in the array
        for i in range(len(bending_section)):

            # If the bending has — sign with an ending
            if '-' in bending_section[i]:

                # Remove the - sign and combine the ending with the word
                bending_section[i] = bending_section[i].replace('-', '')

                # Append the result
                self.bending.append(self.word + bending_section[i])
            
            # Else if the bendign is a whole word
            else:

                # Append the result
                self.bending.append(bending_section[i])

    
    # MARK: Pronunciation def
    def pronun_procc(self, article):

        # Find
        pronunciation_section = article.find('div', id='id-udt')

        # Return
        return pronunciation_section.find('span', class_='lydskrift').text

    
    # MARK: Meaning def
    def meaning_procc(self, article):

        # Find section with all the definitions and examples
        meaning_section = article.find_all('div', class_='definitionIndent')

        for i in range(len(meaning_section)):

            # If in the meaning section contains an element with id='betydning-{i}'
            if meaning_section[i].find('div', id=f'betydning-{i+1}'):

                # Go to the element
                path = meaning_section[i].find('div', id=f'betydning-{i+1}')

                # Save definition
                definition = path.find('span', class_='definition').text.replace('\xa0', '-')
                
                # If there is an exiting example
                if path.parent.find('span', class_='citat'):

                    # Save the example
                    example = path.parent.find('span', class_='citat').text
                else:
                    example = None

                # Append a Meaning object with definition and example
                self.meanings.append(Meaning(translate(definition), example))
            else:

                # Break out of the loop
                break

test = Word(search_word='lys', pos='verb')
print('Word: ' + test.word)
print('Part of Speech: ' + test.pos)
print('Gender: ' + test.gender)
print('Bending: ', end = '')
print(test.bending)
print('Pronunciation: ' + test.pronunciation)
print('Definition 1: ' + test.meanings[0].definition)
print('Example: ' + test.meanings[0].example)