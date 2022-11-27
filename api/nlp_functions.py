"""File to define the NLP functions."""
import os
import torch
import spacy
from api.logger import logger

# --------------------------
# Spacy initialisation
# Get model name from environment variable
SPACY_MODEL = os.environ.get('SPACY_MODEL', 'en_core_web_trf')
# Get GPU enabled from environment variable
GPU_ENABLED = os.environ.get('GPU_ENABLED', False)

try:
    logger.info(f"Loading Spacy Model {SPACY_MODEL}")
    # Add additional check for CUDA being available to torch - GPUs are not available during build
    if GPU_ENABLED and torch.cuda.is_available():
        logger.info("GPU Enabled")
        spacy.require_gpu()
    else:
        logger.info("GPU Off")
    nlp = spacy.load(SPACY_MODEL)
except OSError:
    logger.warning("Spacy Model Load Error")
    nlp = spacy.load('en_core_web_sm')
# --------------------------


def process_text(text: str):
    """Process text with spaCy."""
    doc = nlp(text)
    noun_phrases = [chunk.text for chunk in doc.noun_chunks]
    return noun_phrases
