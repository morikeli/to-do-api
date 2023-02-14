from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TasksSerializer
from .models import Tasks

@api_view(['GET', 'POST'])
def schedule_task_view(request):
    if request.method == 'GET':
        scheduled_task = Tasks.objects.all()
        serializer = TasksSerializer(scheduled_task, many=True)
        
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT', 'DELETE'])
def edit_tasks_view(request, pk):
    try:
        task = get_object_or_404(Tasks, id=pk)
    except Tasks.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TasksSerializer(task)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = TasksSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

