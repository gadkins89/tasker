from rest_framework.views import APIView
from task.models import Task
from task.serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

class TaskList(APIView):

    def get(self, request):
        locations = Task.objects.all() # complex data
        serializer = TaskSerializer(locations, many=True)
        return Response(serializer.data)
    
    
class TaskCreate(APIView):

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class TaskDetail(APIView):

    def getTaskByPk(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Task does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        task = self.getTaskByPk(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    def put(self, request, pk):
        task = self.getTaskByPk(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        task = self.getTaskByPk(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    