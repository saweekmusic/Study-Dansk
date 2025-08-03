from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
model = "gemini-2.5-flash-lite-preview-06-17"

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
    client = AIClientInit()

    # Import the AI request prompt
    with open('src/AIPromts/WordsRequest.json', 'r') as file:
        prompt_data = json.load(file)

    prompt = f'Please provide a list of five unique {pos} in lowercase, separated by commas only — no other output, no punctuation at the end. The words must match {DUlevel} level and module, and be related to the topic/theme "{topic}".\n{json.dumps(prompt_data, indent=2)}'
    response = client.models.generate_content(model = model, contents=prompt).text

    if response:
        return response.split(', ')
    raise ValueError("No words returned from AI request.")

def askExampleAI(phrase: str, meaning: str) -> str:
    # TODO: Finish the function
    client = AIClientInit()
    prompt = f'Provide an example sentence in danish for the word "{phrase}" in the meaning of "{meaning}". Only return the sentence only, in one line, with no additional explanations.'
    response = client.models.generate_content(
        model = model, contents=prompt
    ).text

    if response:
        return response.strip()
    raise ValueError("No example returned from AI request.")

