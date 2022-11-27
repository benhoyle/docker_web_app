"""File to define tasks to be performed by celery workers."""
import os
from celery import Celery
from celery.signals import after_setup_logger
from api.logger import consoleHandler
from api.nlp_functions import process_text

# Get user defined broker details
BROKER_URI = os.environ.get('BROKER_URI', 'amqp://guest:guest@localhost:5672/')
BACKEND_URI = os.environ.get('BACKEND_URI', 'redis://localhost:6379/0')
celery_app = Celery('tasks', broker=BROKER_URI, backend=BACKEND_URI)


# Setup logging by augmenting the celery logger as per: https://www.distributedpython.com/2018/08/28/celery-logging/
@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    """Setup logging for celery."""
    # Add journal handler to celery logger
    logger.addHandler(consoleHandler)


@celery_app.task()
def nlp_process(text: str):
    """Task to process text."""
    noun_phrases = process_text(text)
    return noun_phrases
