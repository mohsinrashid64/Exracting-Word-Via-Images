import os
import base64
from fastapi import HTTPException

def encode_image(image_content):
    try:
        encoded_image = base64.b64encode(image_content)
        return encoded_image.decode('utf-8')
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error encoding image.")


def extract_file_type(file_path):
    _, file_extension_with_dot = os.path.splitext(file_path)
    return file_extension_with_dot[1:]

