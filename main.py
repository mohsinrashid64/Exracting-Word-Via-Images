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
# async def extract_text_from_image(attribute_name: str, file: UploadFile = File(...), tax_status: bool = False):
async def extract_text_from_image(attribute_name: str, file: UploadFile = File(...)):
    file_content = await file.read()  # Read the contents of the uploaded file as bytes
    base64_image = encode_image(file_content)  # Encode the file content in base64

    value = getattr(config, attribute_name, None)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
    }

    try:
        payload = {
            'model': "gpt-4o",
            'messages': value + [{
                "role": "user",
                "content": [{
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/{extract_file_type(file.filename)};base64,{base64_image}"
                    }
                }]
            }],
            'max_tokens': 1000,
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()['choices'][0]['message']['content']
        
        json_response = response_data
        data = json.loads(json_response)
        
        # # Calculate tax if tax_status is True
        # if tax_status:
        #     data['tax'] = calculate_tax(data)  # Implement your tax calculation logic
        # else:
        #     print('TAX STATUS IS SET  TO FALS')

        return {'response': data}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error,{e}")

# Dummy tax calculation function
def calculate_tax(data):
    # Implement your tax calculation logic here
    tax_amount = 0
    print('CALCULATE TAX EXECUTED')
    # # Example logic:
    # if 'amount' in data:
    #     tax_amount = data['amount'] * 0.1  # Example: 10% tax
    return tax_amount