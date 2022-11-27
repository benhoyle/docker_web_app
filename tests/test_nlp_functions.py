"""Separate file to test the NLP functions."""
from api.nlp_functions import process_text


def test_process_text():
    """Test normal processing."""
    noun_phrases = process_text("This is a test")
    assert noun_phrases == ['This', 'a test']

