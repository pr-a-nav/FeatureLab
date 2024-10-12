from typing import Annotated
from fastapi import FastAPI, UploadFile , File
import pandas as pd

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/files/")
async def create_file(file ):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
     print("good thing")
     if not file:
        return {"message": "No upload file sent"}
     else:
        data = pd.read_csv(file.file)
        print(data.shape)
        return {"filename": file.filename , "data": data.shape}