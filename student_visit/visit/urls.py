from django.urls import path
from .views import AddStudent, VisitStudent,schema_view

urlpatterns = [
    path('add-student/<int:pk>', AddStudent.as_view(), name='add-student'),
    path('add-student', AddStudent.as_view(), name='add-student'),
    path('visit-student', VisitStudent.as_view(), name='visit-student'),
    path('visit-student/<int:pk>/', VisitStudent.as_view(), name='visit-student-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
