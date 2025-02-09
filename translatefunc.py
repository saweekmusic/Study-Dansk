import requests
import json
import os

with open('authorisation.txt') as file:
    auth = file.readline()
    

def translate(text: str):
    url = "https://api-b2b.backenster.com/b1/api/v3/translate"

    payload = {
        "platform": "api",
        "from": "da_DK",
        "to": "en_US",
        "data": text
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": os.getenv("TRANSALTE_AUTH")
    }

    # # response = requests.post(url, json=payload, headers=headers).text
    # data = json.loads(response)
    # return data["result"]
    return text