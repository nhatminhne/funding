from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Backend.models import Contribution, Projects, Users
from Backend.serializers import ContributionSerializer, ProjectSerializer, UserSerializer

# Create your views here.
@csrf_exempt
def projectAPI(request, id=0):
    if request.method == 'GET':
        projects = Projects.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)
    elif request.method == 'POST':
        project_data = JSONParser().parse(request)
        project_serializer = ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        project = Projects.objects.get(projectID=project_data['projectID'])
        project_serializer = ProjectSerializer(project, data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        project = Projects.objects.get(projectID=id)
        project.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def userAPI(request, id=0):
    if request.method == 'GET':
        users = Users.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = Users.objects.get(userID=user_data['userID'])
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        user = Users.objects.get(userID=id)
        user.delete()
        return JsonResponse("Deleted successfully", safe=False)

@csrf_exempt
def contributionAPI(request, id=0):
    if request.method == 'GET':
        contribution = Contribution.objects.all()
        contribution_serializer = ContributionSerializer(contribution, many=True)
        return JsonResponse(contribution_serializer.data, safe=False)
    elif request.method == 'POST':
        contribution_data = JSONParser().parse(request)
        contribution_serializer = ContributionSerializer(data=contribution_data)
        if contribution_serializer.is_valid():
            contribution_serializer.save()
            return JsonResponse("Added successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        contribution_data = JSONParser().parse(request)
        contribution = Contribution.objects.get(contributionID=contribution_data['contributionID'])
        contribution_serializer = ContributionSerializer(contribution, data=contribution_data)
        if contribution_serializer.is_valid():
            contribution_serializer.save()
            return JsonResponse("Update successfully", safe=False)
        return JsonResponse("Failed to update")
    elif request.method == 'DELETE':
        contribution = Contribution.objects.get(contributionID=id)
        contribution.delete()
        return JsonResponse("Deleted successfully", safe=False)
