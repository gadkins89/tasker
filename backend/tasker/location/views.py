# from django.shortcuts import render
# from location.models import Location
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from location.serializer import LocationSerializer

# # Create your views here.
# @api_view(['GET'])
# def locationList(request):
#     locations = Location.objects.all() # complex data
#     serializer = LocationSerializer(locations, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def locationCreate(request):
#     serializer = LocationSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def location(request, pk):

#     try:
#         location = Location.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Location does not exist'
#         }, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = LocationSerializer(location)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = LocationSerializer(location, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from location.models import Location
from location.serializer import LocationSerializer
from rest_framework.response import Response
from rest_framework import status

class LocationList(APIView):

    def get(self, request):
        locations = Location.objects.all() # complex data
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)
    
    
class LocationCreate(APIView):

    def post(self, request):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class LocationDetail(APIView):

    def getLocationByPk(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Location does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
        
    def get(self, request, pk):
        location = self.getLocationByPk(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
    
    def put(self, request, pk):
        location = self.getLocationByPk(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        location = self.getLocationByPk(pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    