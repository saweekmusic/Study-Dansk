# Supabase API functions
import os
from dotenv import load_dotenv
from supabase import create_client, Client
from idioms import Idiom
from meanings import Meaning

# Load environment variables from .env file
load_dotenv()

# Initialize Supabase client
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


# MARK: Supabase API functions
# Function to insert a word into the "words" table
def insert_word(self):

    # Insert the word data into the "words" table
    response = supabase.table("words").insert(
        {
            "word": self.word,
            "pronunciation": self.pronunciation,
            "determiner": self.determiner,
            "pos": self.pos,
            "bendings": self.bendings
        }
    ).execute()

    # Return the ID of the inserted word
    return response.data[0]["id"]


# Function to insert idioms into the "idioms" table
def insert_idioms(self):
    idioms_id = []

    # Iterate over each idiom in the self.idioms list
    for idiom in self.idioms:

        # Insert the idiom data into the "idioms" table
        idiomResponse = supabase.table("idioms").insert(
            {
                "idiom": idiom.idiom,
                "idiom_en": idiom.idiom_en
            }
        ).execute()

        # Append the ID of the inserted idiom to the idioms_id list
        idioms_id.append(idiomResponse.data[0]["id"])

    # Return the list of inserted idiom IDs
    return idioms_id


# Function to insert word meanings into the "word_meanings" table
def insert_word_meanings(self, word_id):

    # Iterate over each meaning in the self.meanings list
    for meaning in self.meanings:

        # Insert the meaning data into the "word_meanings" table
        supabase.table("word_meanings").insert(
            {
                "word_id": word_id,
                "definition": meaning.definition,
                "definition_en": meaning.definition_en,
                "example": meaning.example,
                "example_en": meaning.example_en,
            }
        ).execute()


# Function to insert idiom meanings into the "idiom_meanings" table
def insert_idiom_meanings(self, idioms_id):

    # Iterate over each idiom ID in the idioms_id list
    for i, idiom_id in enumerate(idioms_id):

        # Iterate over each meaning in the self.idioms[i].meanings list
        for meaning in self.idioms[i].meanings:

            # Insert the meaning data into the "idiom_meanings" table
            supabase.table("idiom_meanings").insert(
                {
                    "idiom_id": idiom_id,
                    "definition": meaning.definition,
                    "definition_en": meaning.definition_en,
                    "example": meaning.example,
                    "example_en": meaning.example_en,
                }
            ).execute()


# Function to insert word-idiom connections into the "words_idioms" table
def insert_word_idiom_connections(word_id, idioms_id):

    # Iterate over each idiom ID in the idioms_id list
    for idiom_id in idioms_id:

        # Insert the word-idiom connection data into the "words_idioms" table
        supabase.table("words_idioms").insert(
            {
                "word_id": word_id,
                "idiom_id": idiom_id
            }
        ).execute()


# Main function to push a word and its related data to the database
def pushWordDB(self):
    word_id = insert_word(self)
    idioms_id = insert_idioms(self)
    insert_word_meanings(self, word_id)
    insert_idiom_meanings(self, idioms_id)
    insert_word_idiom_connections(word_id, idioms_id)


# Placeholder function for fetching a word from the database
def fetchWordDB(self, search_word: str, pos: str):

    # Fetch the word data from the database
    wordT = (supabase.table("words")
                        .select("*")
                        .eq("word", search_word)
                        .eq("pos", pos)
                        .execute())
    
    wordMeaningsT = (supabase.table("word_meanings")
                        .select("*")
                        .eq("word_id", wordT.data[0]["id"])
                        .execute())
    
    wordsIdiomsT = (supabase.table("words_idioms")
                        .select("*")
                        .eq("word_id", wordT.data[0]["id"])
                        .execute())
    
    idiomsT = (supabase.table("idioms")
                        .select("*")
                        .in_("id", [wordsIdiom["idiom_id"] for wordsIdiom in wordsIdiomsT.data])
                        .execute())
    
    idiomMeaningsT = (supabase.table("idiom_meanings")
                        .select("*")
                        .in_("idiom_id", [idiom["id"] for idiom in idiomsT.data])
                        .execute())

    # Assign values from the database to the variables in self
    self.word = wordT.data[0]["word"]
    self.pronunciation = wordT.data[0]["pronunciation"]
    self.pos = wordT.data[0]["pos"]
    self.determiner = wordT.data[0]["determiner"]
    self.bendings = wordT.data[0]["bendings"]

    # Assign meanings and idioms from the database to the variables in self
    # Iterate over each wordMeaning in wordMeaningsT.data
    for wordMeaning in wordMeaningsT.data:

        # Append a Meaning object to the self.meanings list
        self.meanings.append(Meaning(wordMeaning["definition"], wordMeaning["definition_en"], wordMeaning["example"], wordMeaning["example_en"]))
    
    # Iterate over each idiom in idiomsT.data
    for idiom in idiomsT.data:

        # Create an Idiom object
        idiomObj = Idiom(idiom["idiom"], 
                         idiom["idiom_en"])
        
        data = (supabase.table("idiom_meanings")
                        .select("*")
                        .eq("idiom_id", idiom["id"])
                        .execute())

        # Iterate over each Meaning in idiom
        for meaning in data.data:
            idiomObj.add_meaning(Meaning(meaning["definition"], 
                                        meaning["definition_en"], 
                                        meaning["example"], 
                                        meaning["example_en"]))
        
        # Append the idiomObj to the self.idioms list
        self.idioms.append(idiomObj)


def is_word(search_word: str, pos: str) -> bool:
    # Check if the word exists in the "words" table
    response = supabase.table("words").select("*").eq("word", search_word).eq("pos", pos).execute()
    return len(response.data) > 0