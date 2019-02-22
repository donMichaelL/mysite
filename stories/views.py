from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Story
from .serializers import StorySerializer


class StoriesListApiView(ListAPIView):
    queryset = Story.objects.all()
    serializer_class = StorySerializer
