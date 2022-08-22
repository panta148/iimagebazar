from django.shortcuts import render
from main.models import Images
from .serializers import ImageSerializer
from rest_framework import viewsets
from main.models import Images


class Showdata(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
