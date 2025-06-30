from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from generator import generate_content
from pdf_generator import generate_pdf
from ppt_generator import generate_ppt

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Content Generator is running!"}

@app.post("/generate")
async def generate(
    topic: str = Form(...),
    content_type: str = Form(...)
):
    content = generate_content(topic, content_type)

    if content_type in ["blog", "report"]:
        generate_pdf(content, output_path="output/output.pdf")
        return JSONResponse(content={"message": f"{content_type} saved to PDF."})
    elif content_type == "ppt":
        generate_ppt(topic, content, output_path="output/output.pptx")
        return JSONResponse(content={"message": "PPT saved."})
    else:
        return JSONResponse(content={"message": "Invalid type"})
