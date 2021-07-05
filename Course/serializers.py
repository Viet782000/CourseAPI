from rest_framework import serializers
from Course.models import Course
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    Course = serializers.PrimaryKeyRelatedField(many=True, queryset=Course.objects.all())
    owner = serializers.ReadOnlyField(source='owner.username')
    
    
    class Meta:
        model = User
        fields = ['id', 'username', 'Course', 'owner']


class CourseSerializer(serializers.ModelSerializer):


    class Meta:
        model = Course
        fields = ['id', 'title', 'created', 'content']