from src.Modules.MeaningClass import Meaning

class Idiom:

    def __init__(self, idiom: str, idiom_en: str):
        self.idiom: str = idiom
        self.idiom_en: str = idiom_en
        self.meanings: list[Meaning] = []

    
    def add_meaning(self, meaning: Meaning):
        self.meanings.append(meaning)