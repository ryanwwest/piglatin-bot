# -*- coding: utf-8 -*-
import requests
import json
import os
import re
from googletrans import Translator

BOT_ID = os.environ['BOT_ID']
SENDER_ID = '812538'

translator = Translator()
groupme_url = 'https://api.groupme.com/v3/bots/post'

def send_to_groupme(text):
    data = { "bot_id"  : BOT_ID, "text" : text }
    response = requests.post(groupme_url, json=data)

def post_spanish(text):
    # remove first word
    text = text.split(' ', 1)[1]
    translated = '🇪🇸 ' + translator.translate(text, dest='es').text
    send_to_groupme(translated)

def post_pig_latin(req):
    # remove trigger word 'piglatinfy'
    words = str(req).lower().split()[1:]
    text = '🐷🤖 '
    
    for w in words:
        # remove everything but alphanumeric
        w = re.sub(r'\W+', '', w)
        if len(w) <= 1:
            text += w + ' '
        else:
            text +=  w[1:] + w[0] +'ay '
    send_to_groupme(text)
    

# only respond with piglatin if the user's text starts with 'piglatinfy'
def starts_with_str(req, start_str):
    start_str += ' '
    a = str(req["text"]).lower()
    return a.startswith(start_str) and req["sender_id"] != SENDER_ID

def process(req):
        if starts_with_str(req, 'piglatinfy'):
            post_pig_latin(req["text"])
        if starts_with_str(req, 'spanishfy'):
            post_spanish(req["text"])
