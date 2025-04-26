from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# openai = OpenAI API instance
openai = OpenAI(api_key=os.getenv("OPENAI_AUTH"), project=os.getenv("OPENAI_PROJECT_ID"))

# DUlevel = requested Danskuddannelse level
# topic = subject for word search
# pos = part of speech (e.g., verb, noun, adjective)
def askWordsAI(openai: OpenAI, DUlevel: str, topic: str, pos: str) -> list[str]:
    """Return a list of 5 unique words in Danish for a provided level student in the topic of the given part of speech."""

    prompt = f"Provide 5 unique {pos} words in Danish for a {DUlevel} student in the topic of {topic}, progressively increasing in difficulty. Ensure all words are of the correct {pos} and distinct from previous levels, separated by commas. Only return the words in one line, with no additional explanations."
    # response = openai.ask(prompt).split(", ")
    return ['tælle', 'addere', 'dividere', 'subtrahere', 'løse']


def askExampleAI(openai: OpenAI, phrase: str, meaning: str) -> str:
    # TODO: Finish the function
    prompt = f"Provide an example sentence in danish for the word '{phrase}' in the meaning of '{meaning}'. Only return the sentence only, in one line, with no additional explanations."
    return

