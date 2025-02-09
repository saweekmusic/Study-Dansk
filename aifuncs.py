from openai import OpenAI

# openai = OpenAI API instance
# DUlevel = requested Danskuddannelse level
# topic = subject for word search
# pos = part of speech (e.g., verb, noun, adjective)
def askWords(openai: OpenAI, DUlevel: str, topic: str, pos: str):
    prompt = f"Provide 5 unique {pos} words in Danish for a {DUlevel} student in the topic of {topic}, progressively increasing in difficulty. Ensure all words are of the correct {pos} and distinct from previous levels, separated by commas. Only return the words in one line, with no additional explanations."
    return