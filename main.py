import os
from urllib import response
import aiohttp
from io import BytesIO
from typing import Optional
from urllib.parse import urlparse

from PIL import Image,ImageEnhance
from pydantic import BaseModel
from fastapi import FastAPI,HTTPException
from fastapi.responses import StreamingResponse
 
 
app = FastAPI(
    title="sqy-image-extension",
    description="Use this API to get the image extension",
    version="2.0.1",
)

 
class URL(BaseModel):
    url_: str
 

def extract_filename(URL):
    parsed = urlparse(URL)
    return os.path.basename(parsed.path)


@app.post("/sqy_extension")
async def extension(check_image: URL): 

    '''This function get image URL from user and tell 
    the image extension as a output
    '''
    URL1 = check_image.url_
    filename = extract_filename(URL1)

    filename = filename.strip()

    async with aiohttp.ClientSession() as session:
        async with session.get(URL1) as resp:
            contents = await resp.read()
  
    async with aiohttp.ClientSession() as session:
        async with session.get(URL1) as resp:
            contents = await resp.read()

    if contents == None:
        raise HTTPException(status_code=406, detail="No image found.")

    try:
        image = Image.open(BytesIO(contents))
        result = "."+image.format.lower()
        URL1 = URL1 + result

    except Exception:
        raise HTTPException(status_code=406, detail="Not a valid URL")
 
    if URL1.lower().endswith((".jpg", ".png", ".jpeg", ".gif", ".webp",".jfif")) == False:
        raise HTTPException(status_code=406, detail="Not a valid URL")


    extension = result    
    return extension
