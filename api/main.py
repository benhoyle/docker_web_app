"""Initial API Front End"""
from fastapi import FastAPI
from api.nlp_functions import process_text
from api.celery_tasks import nlp_process
from api.data_models import TextData

# Instantiate the class
app = FastAPI()


# Define a GET method on the specified endpoint
@app.get("/")
def root():
    return {"result": "Welcome to the NLP API"}


# Process text with spaCy
@app.post("/process")
def process(data: TextData):
    """Process text with spaCy."""
    noun_phrases = process_text(data.text)
    return {"noun_phrases": noun_phrases}


# Process with backend queue
@app.post("/delayed_process")
def delayed_process(data: TextData):
    """Process text with spaCy using the backend celery queue."""
    noun_phrases = nlp_process.delay(data.text).get()
    return {"noun_phrases": noun_phrases}
