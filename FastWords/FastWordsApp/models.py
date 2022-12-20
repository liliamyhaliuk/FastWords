from django.db import models
# from django.db.models import Model

class TypingBox(models.Model):
    entered_text = models.TextField(max_length=300)
