# Local Classes
from exampleclass import Meaning
from expressionsclass import Expressions

# Import libreries
import requests
from bs4 import BeautifulSoup
from translatefunc import * 

class Word:
    word = None
    partofspeech = None
    gender = None
    bending = []
    pronunciation = None
    meanings = []
    expressions = []

    def __init__(self, search_word):
        source = requests.get(f'https://ordnet.dk/ddo/ordbog?query={search_word}').text
        soup = BeautifulSoup(source, 'html.parser')
        article = soup.find('div', class_='artikel')

        try:
            article.find('span', class_='match').text
        except AttributeError:
            print('There is no such word.')
            return

        # Word
        word = article.find('span', class_='match')
        if word:
            super_class = word.find('span', class_='super')
            if super_class:
                super_class.decompose()
            self.word = word.text
        else:
            return

        #Part of Speech
        word_info = article.find('span', class_='tekstmedium allow-glossing').text
        word_info = word_info.split(', ')
        self.partofspeech = word_info[0]

        # Gender
        if self.partofspeech == 'substantiv':
            if word_info[1] == 'intetkøn':
                self.gender = 'et'
            elif word_info[1] == 'fælleskøn':
                self.gender = 'en'
        elif self.partofspeech == 'verbum':
            self.gender = 'at'

        # Bending
        bending_section = article.find('div', id='id-boj')
        bending_section = bending_section.find('span', class_='tekstmedium allow-glossing').text.strip().split(', ')
        for i in range(len(bending_section)):
            if '-' in bending_section[i]:
                bending_section[i] = bending_section[i].replace('-', '')
                self.bending.append(self.word + bending_section[i])
            else:
                self.bending.append(bending_section[i])

        # Pronunciation
        pronunciation_section = article.find('div', id='id-udt')
        self.pronunciation = pronunciation_section.find('span', class_='lydskrift').text

        # Examples
        examples_section = article.find('div', id='content-betydninger')
        examples_section = examples_section.find_all('span', class_='definition')

        for i in range(len(examples_section)):
            meaning = Meaning()
            meaning.definition = examples_section[i].text
            # meaning.definition = translate(meaning.definition)
            self.meanings.append(meaning)

        # Expressions
        expressions_section = article.find('div', id='content-betydninger')
        expressions_section = expressions_section.find_all('span', class_='definition')

        for i in range(len(expressions_section)):
            expression = Expressions()
            expression = expressions_section[i].text
            # meaning.definition = translate(meaning.definition)
            self.meanings.append(meaning)
    

test = Word('hjem')
print(test.word)
print(test.partofspeech)
print(test.gender)
print(test.bending)
print(test.pronunciation)
print(test.meanings[0].definition)
print(test.expressions)