"""File to test celery tasks."""
from api.celery_tasks import nlp_process


# This is still looking for an amqp broker despite the conftest in memory broker
# def test_process_text(celery_worker):
#     """Test celery processing."""
#     noun_phrases = nlp_process.delay("This is a test")
#     assert noun_phrases.get() == ['This', 'a test']
