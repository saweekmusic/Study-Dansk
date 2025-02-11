import os
from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase = create_client(url, key)

word = supabase.table("words").select("*").execute().data[0]
word_meanings = supabase.table("word_meanings").select("*").eq("word_id", word["id"]).execute().data
idioms = []
idiom_meanings = []


for pair in supabase.table("words_idioms").select("*").eq("word_id", word["id"]).execute().data:
    for idiom in pair["idiom_id"]:
        idioms.append(supabase.table("idioms").select("*").eq("id", idiom).execute().data)


print()