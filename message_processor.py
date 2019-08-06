# -*- coding: utf-8 -*-
import requests
import json
import os
import re

BOT_ID = os.environ['BOT_ID']
SENDER_ID = '812538'

def send_to_groupme(text):
	data = { "bot_id"  : BOT_ID, "text" : text }
	response = requests.post('https://api.groupme.com/v3/bots/post', json=data)

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
def starts_with_piglatinfy(req):
    a = str(req["text"]).lower()
    return a.startswith('piglatinfy') and req["sender_id"] != SENDER_ID

def process(req):
        if starts_with_piglatinfy(req):
            post_pig_latin(req["text"])
