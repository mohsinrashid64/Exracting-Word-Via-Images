from fastapi import HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from openai import OpenAI
import config
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {'response': "API RUNNING"}


@app.get("/extract_text_from_image")
def extract_text_from_image(image_url: str):
    try:
        client = OpenAI(
            api_key=config.OPENAI_API_KEY,
        )

        response = client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an experienced mobile developer, a web scraper, and an expert in image processing and generative AI. You will be provided with an image, which could be a screenshot of a document or PDF, or it could contain handwritten text. Your task is to extract all of the relevant data from the image and return it in a specified format."
                },
                {
                    "role": "user",
                    "content": [{
                                    "type":"text", 
                                    "text":"What: Please help me extract the textual pieces of information from the image provided.\n\nWho: I am a professional Mobile application developer in Flutter.\n\nWhy: This question originates from a company that makes mobile applications. They are making an e-commerce app and they intend to add a feature in their app that allows the user to upload images and use generative AI to extract the relevant data from the image.\n\nWhich: The data you are supposed to extract from the image is 'Balance Sheet Date', 'Cash', 'Bank', 'Product List' (this could be more than one and have the following attributes): 'Product Name', 'Quantity', 'Delivery Charges', and 'Cost'. The wording of the aforementioned fields may differ so extract according to the meaning. Please ignore anything else.\n\nHow: Finally, return the data as a JSON response."
                                },
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": image_url
                                    }
                                }
                    ]
                }
            ],
            max_tokens=1000,
        )

        return {'response': response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")



@app.get("/image/{filename}")
async def get_image(filename: str):
    image_directory = f"D:/DigiMark/Exracting Word Via Images/data"
    image_path = f"{image_directory}/{filename}"
    return FileResponse(image_path)


