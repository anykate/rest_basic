from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RoomSerializer, StudentSerializer, StudentDetailSerializer
from .models import Room, Student


# Create your views here.
class RoomAPIView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response({'rooms': serializer.data})


class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response({'students': serializer.data})


class StudentDetailAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentDetailSerializer(students, many=True)
        return Response({'students': serializer.data})
