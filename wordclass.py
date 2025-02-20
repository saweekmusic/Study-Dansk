# MARK: Imports
from meanings import Meaning
from idioms import Idiom
from consts import EN_TO_DK
from translatefunc import translate
from scraper import findURL
from apifuncs import is_word, fetchWordDB, pushWordDB


# MARK: Class Word
class Word:

    def __init__(self, search_word: str = None, pos: str = None):
        # Init of attributes
        self.word: str = None
        self.pronunciation: str = None
        self.pos: str = None
        self.determiner: str = None
        self.bendings: list[str] = []
        self.meanings: list[Meaning] = []
        self.idioms: list[Idiom] = []

        # If nothing is passed
        if not search_word and not pos:
            return
        
        # If word exist in the API response
        if is_word(search_word, EN_TO_DK[pos]):

            # Assign values from API to the variables in self
            fetchWordDB(self, search_word, EN_TO_DK[pos])
            return


        # Scrape the word
        article = findURL(search_word=search_word, pos=pos)

        # Apply the data
        self.word = getWord(article)
        self.pronunciation = getPronunciation(article)
        self.pos = getPOS(article, 0)
        self.determiner = getdeterminer(article, self.pos)
        self.bendings = getBendings(article, self.word)
        getMeaning(self, article)
        getIdioms(self, article)

        # Add the word to the database
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
    
    # Find span with class tekstmedium allow-glossing
    word_info = article.find('span', class_='tekstmedium allow-glossing').text
    
    # Break the span
    word_info = word_info.split(', ')

    # Return requested index
    return word_info[index]


# MARK: Gender def
def getdeterminer(article: str, pos: str) -> str:
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

    # Find span with class lydskrift
    pronunciation = article.find('span', class_='lydskrift').text

    # Return replacing all the wierd chars
    return pronunciation.replace('\xa0', '')


# MARK: Meaning def
def getMeaning(self, article):

    # Find section with all the definitions and examples
    meanings = article.find('div', id='content-betydninger')

    # Append each meaning
    for meaning in extract_meanings(meanings, 'betydning'):
        self.add_meaning(meaning)

    
# MARK: Idioms def
def getIdioms(self, article: str):

    # Find section with the idioms
    expressionsHTML = article.find('div', id='content-faste-udtryk')

    # If there is no section with the idioms
    if not expressionsHTML:
        return

    # For every id="udtryk-{i}" in the section
    for i in range(len(expressionsHTML.find_all('div', id=lambda x: x and x.startswith('udtryk-')))):

        path = expressionsHTML.find('div', id=f'udtryk-{i+1}')
        if not path:
            break

        # Create Idiom object with the idiom and its translation
        idiom = path.find('span', class_='match').text
        idiom_en = translate(idiom)
        idiom_obj = Idiom(idiom, idiom_en)

        # Append a meaning to the Idiom
        for meaning in extract_meanings(expressionsHTML, f'udtryk-{i+1}-betydning'):
            idiom_obj.add_meaning(meaning)

        # Append idiom to the self
        self.add_idiom(idiom_obj)


# MARK: Extract meanings def
def extract_meanings(base_path, id_prefix: str) -> list[Meaning]:
    # Empty array to return later
    meanings = []

    # For each div which id starts with id prefix
    for i in range(len(base_path.find_all('div', id=lambda x: x and x.startswith(id_prefix)))):
        
        # Get inside of the element
        path = base_path.find('div', id=f'{id_prefix}-{i+1}')

        # Break if the element is empty
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