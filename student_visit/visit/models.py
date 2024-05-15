from django.db import models

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phone_number = models.CharField(max_length=13)

class FaceData(models.Model):

    student = models.OneToOneField(to=Student,on_delete=models.CASCADE)
    face_date = models.TextField()

class VisitDay(models.Model):

    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    visit_date = models.DateTimeField(auto_now_add=True)