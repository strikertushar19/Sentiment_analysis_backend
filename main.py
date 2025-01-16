from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metrics.sadness import check_sadness_sentiment
from metrics.happiness import check_happiness_sentiment
from metrics.fearness import check_fearness_sentiment
from metrics.angerness import check_angerness_sentiment
from pydantic import BaseModel


class InputData(BaseModel):
    prompt: str


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/sadness")
def sadness(data: InputData):
    results=[]
    results.append(check_sadness_sentiment(data.prompt))
    return results


@app.post("/happiness")
def happiness(data: InputData):
    results=[]
    results.append(check_happiness_sentiment(data.prompt))
    return results


@app.post("/fearness")
def fearness(data: InputData):
    results = []
    results.append(check_fearness_sentiment(data.prompt))
    return results


@app.post("/angerness")
def angerness(data: InputData):
    results = []
    results.append(check_angerness_sentiment(data.prompt))

    return results

@app.post("/allmetrics")
def allmetrics(data: InputData):
    results = []
    results.append(check_angerness_sentiment(data.prompt))
    results.append(check_fearness_sentiment(data.prompt))
    results.append(check_sadness_sentiment(data.prompt))
    results.append(check_happiness_sentiment(data.prompt))

    return results


@app.get("/")
def home():
    return {"message": "Home page"}
