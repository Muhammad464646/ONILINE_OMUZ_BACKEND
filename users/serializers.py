from rest_framework import serializers
from .models import User,Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ('id', 'name', 'icon')


class TeacherSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'profile_picture', 'skills')