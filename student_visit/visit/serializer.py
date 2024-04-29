from rest_framework import serializers
from .models import Student, FaceData, VisitDay

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'birthday','phone_number']

class FaceDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaceData
        fields = ['id', 'student', 'face_date']

class VisitDaySerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    class Meta:
        model = VisitDay
        fields = ['id', 'student', 'visit_date']
