from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
from dotenv import load_dotenv

load_dotenv()

model_name=os.getenv("MODEL")


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


def predict_sentiment(texts):
    if not texts or not any(text.strip() for text in texts):
        print("Nothing in texts")
        return None

    inputs = tokenizer(
        texts, return_tensors="pt", truncation=True, padding=True, max_length=512
    )
    with torch.no_grad():
        outputs = model(**inputs)
    probabilities = torch.nn.functional.softmax(outputs.logits, dim=-1)
    sentiment_map = {
        0: "Very Negative",
        1: "Negative",
        2: "Neutral",
        3: "Positive",
        4: "Very Positive",
    }
    return [sentiment_map[p] for p in torch.argmax(probabilities, dim=-1).tolist()]
