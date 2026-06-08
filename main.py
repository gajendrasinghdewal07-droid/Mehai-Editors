from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import FileResponse
import os

app = FastAPI()

os.makedirs("uploads", exist_ok=True)

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/edit")
async def edit_video(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {
        "success": True,
        "filename": file.filename,
        "prompt": prompt
    }
