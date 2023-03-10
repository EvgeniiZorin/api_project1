from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

posts = {
    "post1": "message1", 
    "post2": "message2"
}

@app.get('/')
def read_root():
    return {"welcome_message": "welcome to my API!"}

@app.get('/posts')
def get_posts():
    return posts
