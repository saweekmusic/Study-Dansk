from src.Modules.Body import WordContent, TableContent, TextContent
from fpdf.table import Table
from src.Constants import POS_TYPES
import src.Functions.TableContentFunctions as TCF
from typing import Callable
from src.Modules.PDFClass import PDF
from src.Modules.WordClass import Word
from src.Modules.Section import Section
from src.Modules.Body import Body


# ==== SECTION TITLES ====
titles = {
    'Section 1': 'Section 1: Learning Words',
    'Section 2': 'Section 2: Match the Words',
    'Section 3': 'Section 3: Fix the Words',
    'Section 4': 'Section 4: Word Puzzle',
}

# ==== SECTION DESCRIPTIONS ====
descriptions = {
    'Section 1': (
        'In this section you are presented with 15 different words on a specific topic and level in Danish: '
        '5 verbs, 5 nouns, and 5 adjectives. You are also given the definitions of these words in English. '
        'Your task is to learn (or at least try to remember main ideas about the words because you do not have '
        'translation of the words themself) these words and their meanings, and then complete the exercises that follow.'
    ),
    'Section 2': (
        'In this section, you should match the words with their definitions. Both the definitions and the words are shuffled. '
        'Your task is to draw a line from a word to a corresponding to it definition. This will help you reinforce your understanding '
        'of the words and their meanings. You can refer to the words and definitions provided in Section 1.'
    ),
    'Section 3': (
        'In this section, you are given a list of words with their letters jumbled. Your task is to rearrange the letters '
        'to form the correct words. This exercise will help you practice your spelling and reinforce your memory of the words.'
    ),
    'Section 4': (
        'In this section, you find a word search puzzle. The words from Section 1 are hidden in the grid. Your task is '
        'to find and circle all the words. This exercise will help you familiarize yourself with the words and their spelling in a fun and engaging way.'
    ),
}


# ==== SECTION CONTENTS ====
contents = {
    'Section 1': lambda pdf, words, DUlevel, topic: [
        # WordContent(pdf = pdf, words = words, DUlevel = 'A1', topic = 'Animals', pos = POS_TYPES[pos]) for pos in list(POS_TYPES.keys())
        WordContent(pdf = pdf, words = words, DUlevel = DUlevel, topic = topic, pos = 'verb') # for testing purposes
    ],
    'Section 2': lambda pdf, words: [
        TableContent(pdf = pdf, rows = TCF.wordsDefinitions_into_rows(words), table = Table(
            fpdf=pdf,
            v_align='M',
            gutter_height=3, 
            gutter_width=20,
            col_widths=(1, 2),
            text_align='C'
        ))
    ],
    'Section 3': lambda pdf, words: [
        TableContent(
            pdf = pdf, 
            rows = TCF.fixWords_into_rows(words), 
            table = Table(
                fpdf=pdf,
                v_align='M',
                gutter_height=3, 
                gutter_width=20,
                col_widths=(1, 2)
            )
        )
    ],
    'Section 4': lambda pdf, words: [
        TableContent(
            pdf = pdf,
            rows = TCF.wordPuzzle(words),
            table = Table(
                fpdf = pdf,
                borders_layout = 'ALL'
            ),
            square = True
        )
    ]
}
