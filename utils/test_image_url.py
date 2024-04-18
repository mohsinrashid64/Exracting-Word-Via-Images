from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def read_root():
        return {"Data": "IT WORKS"}



@app.get("/image/{filename}")
async def get_image(filename: str):
    # Define the directory where your images are stored
    image_directory = f"D:/DigiMark/Exracting Word Via Images/data"
    # Construct the full path to the requested image file
    image_path = f"{image_directory}/{filename}"
    # Return the image file as a response
    return FileResponse(image_path)
