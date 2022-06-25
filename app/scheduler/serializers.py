# rest_framework
from rest_framework import serializers

# local Django
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    """Serialzer for person candidate/interviewer"""
    class Meta:
        model = Person
        fields = '__all__'

class SearchSerializer(serializers.Serializer):
    candidate_id = serializers.UUIDField()
    interviewer_id = serializers.UUIDField()