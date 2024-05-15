from django.contrib import admin
from .models import *

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name",'birthday','phone_number']

class FaceDataAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name","face_date"]

    def last_name(self, obj):
        return obj.student.last_name

    def first_name(self, obj):
        return obj.student.last_name

class VisitdayAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name",'visit_date']

    def last_name(self, obj):
        return obj.student.last_name

    def first_name(self, obj):
        return obj.student.last_name

admin.site.register(Student, StudentAdmin)
admin.site.register(FaceData, FaceDataAdmin)
admin.site.register(VisitDay, VisitdayAdmin)