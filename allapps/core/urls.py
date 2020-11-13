from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.RoomAPIView.as_view(), name='index'),
    path('students/', views.StudentAPIView.as_view(), name='students'),
    path('student_details/', views.StudentDetailAPIView.as_view(),
         name='student-details'),
]
