from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/tesk-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delet/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET','DELETE'])
def task_list(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks)
    return Response(serializer.data) 


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def task_update(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task , data = request.data)
    
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
    return Response(serializer.errors, status=400)



@api_view(['DELETE'])
def task_delete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted") 