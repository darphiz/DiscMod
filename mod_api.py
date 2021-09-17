import os 
import requests
from dotenv import load_dotenv
load_dotenv()
KEY = os.getenv('API_KEY')



def check_nudity(image):
    r = requests.post("https://api.deepai.org/api/nsfw-detector",data={'image': image,}, headers={'api-key': KEY }).json()
    if r['output']["nsfw_score"] > 0.5:
        nude = True
    else:
        nude = False
    return nude

def check_profanity(message):
    url = f"https://www.purgomalum.com/service/containsprofanity?text={message}"
    contains_profanity = requests.get(url).json()
    if contains_profanity:
        profanity = True
    else:
        profanity = False
    return profanity


