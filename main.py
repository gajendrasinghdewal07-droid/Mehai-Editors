from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <body>
        <h2>Mehai Editor V0</h2>

        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="file"><br><br>

            <input type="text" name="prompt" placeholder="Enter Prompt"><br><br>

            <button type="submit">Upload</button>
        </form>

    </body>
    </html>
    """

@app.post("/upload")
async def upload(
    file: UploadFile = File(...),
    prompt: str = Form(...)
):
    return {
        "message": "Video received successfully",
        "filename": file.filename,
        "prompt": prompt
    }
