
# Image Enhance

Color, Brightness and Sharpness Enhancement Techniques
### -------------------------BEFORE---------------------- 
<img src="imgess/before.jpg" width="475" height="360"> 

### ------------------------AFTER------------------------ 
<img src="imgess/after.jpg" width="485" height="360">

### -------------------------BEFORE---------------------- 
<img src="imgess/bef.jpg" width="475" height="360"> 

### -----------------------AFTER---------------------------
<img src="imgess/aft.jpg" width="485" height="360">

### Requirements
1. Python

2. FastAPI, Uploadfile, File

3. Pillow, ImageEnhance

## FastAPI
```http
  pip install fastApi
```

```http
  GET /uploadfile
```

| Parameter | Type     |

|   `image` | `binary` | 

## Result

Upload image it returns enhance image.

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/ajaybenii/image_enhance.git
```

Go to the project directory

```bash
  cd my-project
```

Install dependencies

```bash
  pip install uvicorn
```

Start the server

```bash
  uvicorn main:app --reload
```

  
## Running Tests

Import TestClient.
```http
  pip install pytest
```
Create a TestClient passing to it your FastAPI.

Create functions with a name that starts with test_ (this is standard pytest conventions).

Use the TestClient object the same way as you do with requests.

To run tests, run the following command

```bash
 pytest test_main.py
```

  
## Support

For support, email ajaybeniwal070@gmail.com

  
