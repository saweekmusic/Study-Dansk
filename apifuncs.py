# Supabase API functions
import os
from dotenv import load_dotenv
from supabase import create_client, Client

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
            "determiners": self.determiners,
            "pos": self.pos,
            "bending": self.bending
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
def insert_word_idiom_connections(self, word_id, idioms_id):

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
    insert_word_idiom_connections(self, word_id, idioms_id)

# Placeholder function for fetching a word from the database
def fetchWordDB():
    return