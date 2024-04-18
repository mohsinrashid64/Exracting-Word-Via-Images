from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import config
from fastapi import FastAPI
from utils import encode_image
import requests



app = FastAPI()



@app.get("/")
def read_root():
    return {'response': "API RUNNING"}


@app.get("/extract_text_from_image")
def extract_text_from_image(image_path: str):
    try:
        base64_image = encode_image(image_path)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="The file path provided does not exist.")
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {config.OPENAI_API_KEY}"
    }
    try:
        payload = {
            'model':"gpt-4-turbo",
            'messages': config.PROMPT + [{
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpg;base64,{base64_image}"
                }
            }]
        }],
            'max_tokens':1000,
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(response.json())
        return response.json()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")




