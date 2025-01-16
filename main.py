from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from metrics.sadness import check_sadness_sentiment
from metrics.happiness import check_happiness_sentiment
from metrics.fearness import check_fearness_sentiment
from metrics.angerness import check_angerness_sentiment
from pydantic import BaseModel
import datetime


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


# Helper function to append logs to a file
def log_to_file(endpoint: str, prompt: str, response: dict):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | Endpoint: {endpoint} | Prompt: {prompt} | Response: {response}\n"
    with open("interaction_logs.txt", "a") as log_file:
        log_file.write(log_entry)


@app.post("/sadness")
def sadness(data: InputData):
    results = [check_sadness_sentiment(data.prompt)]
    log_to_file("/sadness", data.prompt, {"results": results})
    return results


@app.post("/happiness")
def happiness(data: InputData):
    results = [check_happiness_sentiment(data.prompt)]
    log_to_file("/happiness", data.prompt, {"results": results})
    return results


@app.post("/fearness")
def fearness(data: InputData):
    results = [check_fearness_sentiment(data.prompt)]
    log_to_file("/fearness", data.prompt, {"results": results})
    return results


@app.post("/angerness")
def angerness(data: InputData):
    results = [check_angerness_sentiment(data.prompt)]
    log_to_file("/angerness", data.prompt, {"results": results})
    return results


@app.post("/allmetrics")
def allmetrics(data: InputData):
    results = {
        "angerness": check_angerness_sentiment(data.prompt),
        "fearness": check_fearness_sentiment(data.prompt),
        "sadness": check_sadness_sentiment(data.prompt),
        "happiness": check_happiness_sentiment(data.prompt),
    }
    log_to_file("/allmetrics", data.prompt, results)
    return results


@app.get("/")
def home():
    return {"message": "Home page"}
