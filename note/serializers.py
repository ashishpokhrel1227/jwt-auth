from rest_framework import serializers
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        # fields = ('id', 'owner', 'title', 'content')
        fields = ('id', 'title', 'content')
        model = Note
