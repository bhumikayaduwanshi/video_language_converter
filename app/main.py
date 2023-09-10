import shutil
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from extraction.audio_from_video import audio_from_video
from extraction.audio_to_text import audio_to_text

app = FastAPI()


@app.post("/upload/")
async def extract_text_from_mp4(file: UploadFile):
    file_name = file.filename
    video_file_name = f'/home/imentus/Desktop/projects/translator/data/video/{file_name}'
    audio_file_name = f'/home/imentus/Desktop/projects/translator/data/audio/{file_name.replace(".mp4", ".wav")}'

    try:
        # Check if the uploaded file is an MP4 file
        if not file_name.endswith(".mp4"):
            return JSONResponse(content={"error": "Only MP4 files are allowed"}, status_code=400)

        with open(video_file_name, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        audio_from_video(video_file_name, audio_file_name)
        text = audio_to_text(audio_file_name)

        return JSONResponse(content={"extracted_text": text}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
