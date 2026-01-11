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
from .serializers import RegisterSerializer
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # здесь сохраняется пользователь
        return Response(serializer.data, status=status.HTTP_201_CREATED)
