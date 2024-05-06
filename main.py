import os
from src import config
from fastapi import FastAPI, UploadFile, File
from src.utils import encode_image, extract_file_type
import requests
from dotenv import load_dotenv
from fastapi import HTTPException
load_dotenv()
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {'response': "API RUNNING"}


@app.post("/extract_text_from_image")
async def extract_text_from_image(attribute_name: str ,file: UploadFile = File(...)):

    file_content = await file.read() # Read the contents of the uploaded file as bytes
    base64_image = encode_image(file_content) # Encode the file content in base64

    value = getattr(config, attribute_name, None)


    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }
    try:
        payload = {
            'model':"gpt-4-turbo",
            "response_format":{ "type": "json_object" },
            'messages': value + [{
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/" + extract_file_type(file.filename) + f";base64,{base64_image}"
                }
            }]
        }],
            'max_tokens':1000,
        }
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        print(response.json()['choices'][0]['message']['content'] )
        #########################################################################
        # This is just for viewing the Data in file in JSON format              #
        # This saves JSON in output.json file                                   #
        json_response = response.json()['choices'][0]['message']['content']     #
        data = json.loads(json_response)                                        #
        # with open('output.json', 'w') as f:                                     #                                                 
        #     json.dump(data, f, indent=4)                                        #
        #########################################################################

        # print(data)
        return {'response': data}

    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")