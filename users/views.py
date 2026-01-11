from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import generics
from .serializers import TeacherSerializer
from .models import User

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    role = request.data.get('role', 'student')
    
    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username уже существует'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=username, password=password, email=email, role=role)
    serializer = TeacherSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
