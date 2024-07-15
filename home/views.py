from urllib import response
from django.shortcuts import render
from home.models import resume
from rest_framework import viewsets

from home.serializers import resumeSerializer


class resumeViewSet(viewsets.ModelViewSet):
    queryset = resume.objects.all()
    serializer_class= resumeSerializer
