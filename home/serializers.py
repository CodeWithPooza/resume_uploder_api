from rest_framework import serializers
from . models import resume

class resumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = resume
        fields= "__all__"