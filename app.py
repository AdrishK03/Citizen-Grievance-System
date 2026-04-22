from fastapi import FastAPI
from utils import analyze_text

app = FastAPI(title="Citizen Grievance AI")

@app.get("/")
def home():
    return {"message": "AI Grievance System Running"}

@app.post("/predict")
def predict(text: str):
    result = analyze_text(text)
    return result