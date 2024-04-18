from fastapi import HTTPException
import os
import config
from fastapi import FastAPI
from utils import encode_image, extract_file_type
import requests
from dotenv import load_dotenv
load_dotenv()
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {'response': "API RUNNING"}



@app.get("/extract_text_from_image/")
def extract_text_from_image(file_path: str):

    base64_image = encode_image(file_path)

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }
    try:
        payload = {
            'model':"gpt-4-turbo",
            'messages': config.PROMPT + [{
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/" + extract_file_type(file_path) + f";base64,{base64_image}"
                }
            }]
        }],
            'max_tokens':1000,
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        #########################################################################
        # This is just for viewing the Data in file in JSON format              #
        # This saves JSON in output.json file                                   #
        json_response = response.json()['choices'][0]['message']['content']     #
        data = json.loads(json_response)                                        #
        with open('output.json', 'w') as f:                                     #                                                 
            json.dump(data, f, indent=4)                                        #
        #########################################################################

        return response.json()
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")




