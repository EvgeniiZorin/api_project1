from fastapi import FastAPI
from datetime import datetime
import random
import os
import pandas as pd
import base64

app = FastAPI()

quotes = {
    "1": "Text for quote 1", 
    "2": "Text for quote 2",
    "3": "Text for quote 3",
    "4": "Text for quote 4",
    "5": "Text for quote 5"
}

# df_quotes_mixed = pd.read_csv('quotes_mixed.csv')
df_quotes_mixed_path = os.path.abspath( os.path.join((os.path.dirname( __file__ )), 'quotes_mixed.csv') )
df_quotes_mixed = pd.read_csv(df_quotes_mixed_path)


@app.get('/')
def read_root():
    return {"welcome_message": "welcome to my API!"}

@app.get('/all_quotes')
def get_quotes():
    return df_quotes_mixed.values.tolist()

@app.get('/random_quote')
def get_random_quote():
    random_quote = df_quotes_mixed.sample(1)
    author = random_quote['Author'].item()
    quote_text = random_quote['Quote'].item()
    return { author: quote_text }

@app.get('/echo/')
def echoer(item1:int = 0, item2:str = 'example'):
    return f"item1: {item1}, {type(item1)}; item2: {item2}, {type(item2)}"

@app.get('/image_b64')
def get_image_base64():
    with open('img1.jpg', 'rb') as f:
        data = f.read()
    data2 = base64.b64encode(data)
    return data2

@app.get('/get_certain_image')
def get_certain_image(name):
    name = name.replace('_', '/')
    with open(name, 'rb') as f:
        data = f.read()
    data2 = base64.b64encode(data)
    return data2
