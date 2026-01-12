from rest_framework import serializers
from .models import User,Skill

class SkillSerializer(serializers.ModelSerializer):
    teacher_username = serializers.CharField(source='teacher.username', read_only=True)

    class Meta:
        model = Skill
        fields = ('id', 'teacher', 'teacher_username', 'name', 'icon')


class TeacherSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'bio', 'profile_picture', 'skills')

    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])  # важно хешировать пароль
        user.save()
        return user