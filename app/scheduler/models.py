# standard library
import uuid
from datetime import date

# Django
from django.db import models

PERSON_CHOICES = (('I', 'Interviewer'), ('C', 'Candidate'))

class Person(models.Model):
    """Model for Interviewer/Candidates"""
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=40)
    type = models.CharField(choices=PERSON_CHOICES, max_length=1, default="I")
    
    available_on = models.DateField(default=date.today)

    available_from = models.TimeField()
    available_to = models.TimeField()

    created_on = models.DateField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
