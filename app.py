from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import os

from KidneyDiseaseClassification.utils.common import decodeImage
from KidneyDiseaseClassification.pipeline.prediction import PredictionPipeline

# Environment variables
os.environ["LANG"] = "en_US.UTF-8"
os.environ["LC_ALL"] = "en_US.UTF-8"

# FastAPI app
app = FastAPI(title="Kidney Disease Classification")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Templates
templates = Jinja2Templates(directory="templates")


# Request model
class PredictionRequest(BaseModel):
    image: str


# Initialize model once
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


clApp = ClientApp()


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/train")
def train():
    # os.system("python main.py")
    os.system("dvc repro")
    return {"message": "Training done successfully!"}


@app.post("/predict")
def predict(data: PredictionRequest):
    decodeImage(data.image, clApp.filename)

    result = clApp.classifier.predict()

    print("RESULT =", result)

    return {
        "prediction": str(result)
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8080
    )