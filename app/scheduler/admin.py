# Django
from django.contrib import admin

# local Django
from .models import Person

admin.site.register(Person)