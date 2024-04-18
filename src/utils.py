import os
import base64
from fastapi import HTTPException

def encode_image(file_path):
  try:
    with open(file_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')
  
  except FileNotFoundError:
      raise HTTPException(status_code=404, detail="The file path provided does not exist.")


def extract_file_type(file_path):
    _, file_extension_with_dot = os.path.splitext(file_path)
    return file_extension_with_dot[1:]

