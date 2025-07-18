import random
from src.Modules.WordClass import Word


def wordsDefinitions_into_rows(words_class: list[Word]) -> list[list[str]]:
    words = [w.word for w in words_class]
    defs = [w.meanings[0].definition_en for w in words_class]
    random.shuffle(words)
    random.shuffle(defs)
    return [[w, d] for w, d in zip(words, defs)]