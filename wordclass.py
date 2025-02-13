# MARK: Imports
from meanings import Meaning
from idioms import Idiom
from consts import *
from translatefunc import * 
from scraper import *
from apifuncs import *


# MARK: Class Word
class Word:

    def __init__(self, search_word: str = None, pos: str = None):
        # Init of attributes
        self.word: str = None
        self.pronunciation: str = None
        self.pos: str = None
        self.determiners: str = None
        self.bending: list[str] = []
        self.meanings: list[Meaning] = []
        self.idioms: list[Idiom] = []

        # TODO: Database check

        # API request of the word from the Database
        
        # If word exist in the API response

            # Assign values from API to the variables in self

            # Return


        # Scrape the word
        try:
            article = findURL(search_word=search_word, pos=pos)
        except ValueError as e:
            print(e)
            return None
        

        self.word = getWord(article)
        self.pronunciation = getPronunciation(article)
        self.pos = getPOS(article, 0)
        self.determiners = getDeterminers(article, self.pos)
        self.bending = getBendings(article, self.word)
        getMeaning(self, article)
        getIdioms(self, article)

        # TODO: Add the word to the database
        pushWordDB(self)


    # MARK: Add meaning
    def add_meaning(self, meaning: Meaning):
        self.meanings.append(meaning)

    
    # MARK: Add idiom
    def add_idiom(self, idiom: Idiom):
        self.idioms.append(idiom)



# MARK: Word def
def getWord(article: str) -> str:
    # Find word in the source html
    word = article.find('span', class_='match')

    # If the 'word' has a number after it
    super_element = word.find('span', class_='super')
    if super_element:

        # Remove it from the scope
        super_element.decompose()

    return word.text


# MARK: POS def
def getPOS(article: str, index: int) -> str:
    if index > 1:
        return None
        
    word_info = article.find('span', class_='tekstmedium allow-glossing').text.split(', ')
    return word_info[index]


# MARK: Gender def
def getDeterminers(article: str, pos: str) -> str:
    # If it is a noun
    if pos == 'substantiv':
        return 'et' if getPOS(article, 1) == 'intetkøn' else 'en'
    
    # Else if it is a verb
    elif pos == 'verbum':
        return 'at'
    
    return None


# MARK: Bending def
def getBendings(article: str, word: str) -> list[str]:
    # Get benfing section from the site
    bending_sec = article.find('div', id='id-boj')

    # Find the bending themselves from the section and break them into an array
    bending_sec = bending_sec.find('span', class_='tekstmedium allow-glossing').text.split(', ')

    bendings = []
    # For every bending in the array
    for bending in bending_sec:

        # If the bending has — sign with an ending
        if '-' in bending:

            # Remove the - sign and combine the ending with the word
            bending = bending.replace('-', '')

            # Append the result
            bendings.append(word + bending)
        
        # Else if the bendign is a whole word
        else:

            # Append the result
            bendings.append(bending)

    return bendings


# MARK: Pronunciation def
def getPronunciation(article: str) -> str:

    # Find
    pronunciation = article.find('span', class_='lydskrift').text

    # Return
    return pronunciation.replace('\xa0', '')


# MARK: Meaning def
def getMeaning(self, article):

    # Find section with all the definitions and examples
    meanings = article.find('div', id='content-betydninger')

    for meaning in extract_meanings(meanings, 'betydning'):
        self.add_meaning(meaning)

    
# MARK: Idioms def
def getIdioms(self, article: str):

    # Find section with the idioms
    expressionsHTML = article.find('div', id='content-faste-udtryk')

    # For every id="udtryk-{i}" in the section
    for i in range(len(expressionsHTML.find_all('div', id=lambda x: x and x.startswith('udtryk-')))):

        path = expressionsHTML.find('div', id=f'udtryk-{i+1}')
        if not path:
            break

        # Create Idiom object with the idiom and its translation
        idiom = path.find('span', class_='match').text
        idiom_en = translate(idiom)
        idiom_obj = Idiom(idiom, idiom_en)

        for meaning in extract_meanings(expressionsHTML, f'udtryk-{i+1}-betydning'):
            idiom_obj.add_meaning(meaning)

        self.add_idiom(idiom_obj)


# MARK: Extract meanings def
def extract_meanings(base_path, id_prefix: str) -> list[Meaning]:
    meanings = []
    for i in range(len(base_path.find_all('div', id=lambda x: x and x.startswith(id_prefix)))):
        
        path = base_path.find('div', id=f'{id_prefix}-{i+1}')
        if not path:
            break

        # Save definition
        definition = path.find('span', class_='definition').text.replace('\xa0', '-')
        definition_en = translate(definition)

        # Save the example if it exists
        example_tag = path.parent.find('span', class_='citat')
        example = example_tag.text if example_tag else None
        example_en = translate(example) if example else None

        # Append a Meaning object with definition and example
        meanings.append(Meaning(definition, definition_en, example, example_en))
    return meanings
        
        
test = Word(search_word='lyse', pos='verb')
# print('Word: ' + test.word)
# print('Pronunciation: ' + test.pronunciation)
# print('Part of Speech: ' + test.pos)
# print('Gender: ' + test.gender)
# print('Bending: ', end = '')
# print(test.bending)


# print('Meanings:')
# for meaning in test.meanings:
#     print('    Definition: ' + meaning.definition)
#     print('    Definition (EN): ' + meaning.definition_en)
#     print('    Example: ' + meaning.example if meaning.example else 'None')
#     print('    Example (EN): ' + meaning.example_en if meaning.example_en else 'None')
#     print()

# print('Idioms:')
# for idiom in test.idioms:
#     print('    Idiom: ' + idiom.idiom)
#     print('    Idiom (EN): ' + idiom.idiom_en)
#     for meaning in idiom.meanings:
#         print('        Definition: ' + meaning.definition)
#         print('        Definition (EN): ' + meaning.definition_en)
#         print('        Example: ' + meaning.example if meaning.example else 'None')
#         print('        Example (EN): ' + meaning.example_en if meaning.example_en else 'None')
#         print()



# {'word': 'lyse', 'pronunciation': '[ˈlyːsə]', 'pos': 'verbum', 'gender': 'at', 'bending': ['lyser', 'lyste', 'lyst']}