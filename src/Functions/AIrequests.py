from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

# DUlevel = requested Danskuddannelse level
# topic = subject for word search
# pos = part of speech (e.g., verb, noun, adjective)
def AIClientInit() -> genai.Client:
    '''Initialize and return a Google Gemini AI client.'''
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ImportError("GEMINI_API_KEY not found in the environment variables file.")
    return genai.Client(api_key=api_key)

def askWordsAI(DUlevel: str, topic: str, pos: str) -> list[str]:
    # return ['løse', 'tælle', 'addere', 'dividere', 'subtrahere']

    client = AIClientInit()

    prompt = f'Provide 5 unique {pos} words in Danish for a {DUlevel} student in the topic of {topic}, progressively increasing in difficulty. Ensure all words are of the correct {pos} and distinct from previous levels, separated by commas. Only return the words in one line, with no additional explanations.'
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite-preview-06-17", contents=prompt
    ).text

    if response:
        return response.split(', ')
    raise ValueError("No words returned from AI request.")

def askExampleAI(phrase: str, meaning: str) -> str:
    # TODO: Finish the function
    client = AIClientInit()
    prompt = f'Provide an example sentence in danish for the word \'{phrase}\' in the meaning of \'{meaning}\'. Only return the sentence only, in one line, with no additional explanations.'
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite-preview-06-17", contents=prompt
    ).text

    if response:
        return response.strip()
    raise ValueError("No example returned from AI request.")

