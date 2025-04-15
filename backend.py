# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from geimini import generate_response
from nlp import text_emotion
from rag import my_vector_store
app = FastAPI()
import webbrowser
import os
import json
import re


# Allow CORS for frontend testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or set specific frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define request body schema
class PromptRequest(BaseModel):
    prompt: str

def clean_and_parse_response(response_text):
    # Remove 'json' keyword and clean up
    match = re.search(r'\{.*\}', response_text, re.DOTALL)
    if match:
        clean_json = match.group()
        return json.loads(clean_json)
    return None
# Sample logic (replace this with your actual backend processing)
def process_prompt(query: str) -> str:
    response_given=''
    if query.startswith('activate'):
        if "open youtube" in query:
            webbrowser.open_new("youtube.com")
        elif "open google" in query:
            webbrowser.open_new("google.com")
        elif 'song'in query:
            music_dir= r'E:\new videos\suyash mumbai\songs'
            # print(os.listdir(music_dir))
            os.startfile(os.path.join(music_dir,'birthday.mp3'))
        elif 'code' in query:
            code_dir= r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code"
            os.startfile(code_dir)
            response_given="Here you go!"
    else:
        user_emotion=text_emotion(query)[0]['label']
        vcs=my_vector_store()
        context=''
        if not query=='':
            res=vcs.v_similarity(query=query,k=1)
            print( res)
            for resp, score in res:
                # print('response '+resp)
                print(score)
                context=resp.page_content
        response_total = generate_response(context,query,user_emotion=user_emotion)
        response_given =clean_and_parse_response(response_total)
    return response_given

@app.post("/api/assistant")
async def handle_prompt(request: PromptRequest):
    response = process_prompt(request.prompt)
    return {"response": response['DESCRIPTION'],
            "actions":response['ACTION']}
