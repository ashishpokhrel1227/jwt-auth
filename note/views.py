from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import Note
from .serializers import NoteSerializer

class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class NoteViewSet(viewsets.ModelViewSet):
    # queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = (IsOwner, )

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Note.objects.filter(owner=user)
        raise PermissionDenied()

    def perform_create(self, serialier):
        serialier.save(owner=self.request.user)