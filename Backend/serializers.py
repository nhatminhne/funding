from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Backend.models import Projects

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Projects
        fields=('projectID', 'creatorId', 'name', 'category', 'description', 'image', 'minPrice', 'targetPrice', 'isFeatured', 'total', 'donateCount')