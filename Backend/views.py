from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Backend.models import Projects
from Backend.serializers import ProjectSerializer

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