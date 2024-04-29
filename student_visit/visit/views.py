from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
import image_to_array
from .serializer import *
from .models import *

# Create your views here.

class AddStudent(APIView):

    def get(self,request: Request,pk=False):

        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data,status=HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"message":"does not find"},status=HTTP_404_NOT_FOUND)
        else:
            students = Student.objects.all()
            serializer = StudentSerializer(students,many=True)
            return Response(serializer.data,status=HTTP_200_OK)
        
    def post(self,request: Request):
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            file = request.FILES["file_name"]
            with open(f'images/{file.name}',"wb") as destination:
                destination.write(file)
            face = str(image_to_array.face_encodings_func(f'images/{file.name}'))
            face_write = FaceData.objects.create(student=Student.objects.get(id=serializer.pk),face_data=face)
            return Response(serializer.data,status=HTTP_201_CREATED)
        else:
            return Response({"message":"bad request"},status=HTTP_500_INTERNAL_SERVER_ERROR)
        
class VisitStudent(APIView):

    def get(self,request,pk=False):

        if pk:
            try:
                student = Student.objects.get(id=pk)
                visit = VisitDay.objects.filter(student=student)
                serializer = VisitDaySerializer(visit,many=True)       
                return Response(serializer.data,status=HTTP_200_OK)     
            except Student.DoesNotExist:
                return Response({"message":"does not find"},status=HTTP_404_NOT_FOUND)
        visits = VisitDay.objects.all()
        serializer = VisitDaySerializer(visit,many=True)
        return Response(serializer.data,status=HTTP_200_OK)
    
    def post(self,request: Request):

        file = request.FILES["file_name"]
        with open(f'images/{file.name}',"wb") as destination:
            destination.write(file)

        all_faces = FaceData.objects.values_list("face_data",flat=True)
        id_face = image_to_array.is_true_face(all_faces,f'images/{file.name}')
        if id_face != -1:
            face = all_faces[id_face]
            student = FaceData.objects.get(face_data=face).student
            visit_day = VisitDay.objects.create(student=student)
            serializer = VisitDaySerializer(visit_day)
            return Response(serializer.data,status=HTTP_201_CREATED)
        return Response({"message":"does not find"},status=HTTP_404_NOT_FOUND)

            

