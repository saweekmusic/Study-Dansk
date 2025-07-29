import random
from src.Modules.WordClass import Word
from src.Modules.Cell import TableCell


def wordsDefinitions_into_rows(words_class: list[Word]) -> list[list[TableCell]]:
    words = [w.word for w in words_class]
    defs = [w.meanings[0].definition_en for w in words_class]
    random.shuffle(words)
    random.shuffle(defs)
    return [[TableCell(text = w), TableCell(text = d)] for w, d in zip(words, defs)]

def fixWords_into_rows(words_class: list[Word]):
    words = [w.word for w in words_class]
    random.shuffle(words)

    # Shuffle letters in the words
    for i, word in enumerate(words):
        letters = list(word)
        random.shuffle(letters)
        words[i] = ''.join(letters)
    return [[TableCell(text = word, align = 'L'), TableCell(align = 'L', border = "BOTTOM")] for word in words]  # Return rows with jumbled words and empty definitions