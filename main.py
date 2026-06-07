from fastapi import FastAPI, UploadFile, File
from editor import process_video

app = FastAPI()

@app.get("/")
def home():
    return {"status": "AI Editor running"}

@app.post("/edit")
async def edit_video(file: UploadFile = File(...), prompt: str = ""):
    input_path = f"uploads/{file.filename}"
    
    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = process_video(input_path, prompt)

    return {"video": output_path}
    
    from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from editor import process_video

app = FastAPI()

@app.get("/")
def home():
    return FileResponse("index.html")

@app.post("/edit")
async def edit_video(file: UploadFile = File(...), prompt: str = ""):
    input_path = f"uploads/{file.filename}"

    with open(input_path, "wb") as f:
        f.write(await file.read())

    output_path = process_video(input_path, prompt)

    return {"video": output_path}
