from django.shortcuts import render

from rest_framework import generics
from .models import User,Skill
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer,TeacherSerializer,SkillSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminUser]

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAdminUser]