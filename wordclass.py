# Local Classes
from exampleclass import Meaning
from expressionsclass import Expression

# Import libreries
import requests
from bs4 import BeautifulSoup
from translatefunc import * 

class Word:
    # MARK: Attributes
    word: str = None
    partofspeech: str = None
    gender: str = None
    bending: list[str] = []
    pronunciation: str = None
    meanings: list[Meaning] = []

    # TODO: Implement Expressions
    # expressions: list[Expression] = []


    # MARK: Init definition
    def __init__(self, search_word):

        # Pulling the html code of the requiered word
        source = requests.get(f'https://ordnet.dk/ddo/ordbog?query={search_word}').text
        soup = BeautifulSoup(source, 'html.parser')
        article = soup.find('div', class_='artikel')

        # If the word doesn't exist
        if not article.find('span', class_='match').text:
            return


        # MARK: Assigning Word
        # Find word in the source html
        word = article.find('span', class_='match')

        # If the 'word' has a number after it
        if word.find('span', class_='super'):

            # Remove it from the scope
            word.find('span', class_='super').decompose()

        # Assign
        self.word = word.text


        # MARK: Part of Speech
        word_info = article.find('span', class_='tekstmedium allow-glossing').text
        word_info = word_info.split(', ')

        self.partofspeech = word_info[0]


        # MARK: Assigning Gender
        # If it is a noun
        if self.partofspeech == 'substantiv':

            # And if it is the et-word
            if word_info[1] == 'intetkøn':

                # Assign
                self.gender = 'et'
            
            # Else if it is the en-word
            elif word_info[1] == 'fælleskøn':

                # Assign
                self.gender = 'en'

        # Else if it is a verb
        elif self.partofspeech == 'verbum':

            # Assign
            self.gender = 'at'


        # MARK: Assigning Bending
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


        # MARK: Assigning Pronunciation
        pronunciation_section = article.find('div', id='id-udt')
        self.pronunciation = pronunciation_section.find('span', class_='lydskrift').text


        ## MARK: Assigning Meanings
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


        # # Expressions
        # expressions_section = article.find('div', id='content-faste-udtryk')
        # expressions_section = expressions_section.find_all('span', class_='definition')

        # for i in range(len(expressions_section)):
        #     expression = Expression()
        #     expression = expressions_section[i].text
        #     meaning.definition = translate(meaning.definition)
        #     self.meanings.append(meaning)
    

test = Word('børste')
print('Word: ' + test.word)
print('Part of Speech: ' + test.partofspeech)
print('Gender: ' + test.gender)
print('Bending: ', end = '')
print(test.bending)
print('Pronunciation: ' + test.pronunciation)
print('Definition 1: ' + test.meanings[0].definition)
print('Example: ' + test.meanings[0].example)