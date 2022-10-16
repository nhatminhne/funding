from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Backend.models import Projects, Users, Contribution

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('projectID', 'creatorId', 'name', 'category', 'description', 'image', 'minPrice', 'targetPrice', 'isFeatured', 'total', 'donateCount')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('userID', 'name', 'email', 'image', 'description')

class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ('contributionID', 'userID', 'projectID', 'amount')
