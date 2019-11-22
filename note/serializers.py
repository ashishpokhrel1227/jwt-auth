from rest_framework import serializer
from .models import Note

class NoteSerializer(serializer.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'title', 'content')
        model = Note
        