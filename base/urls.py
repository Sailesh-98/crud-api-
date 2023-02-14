from django.urls import path
from .import views



urlpatterns = [
    path('student-detail/', views.studentdetail  , name="student-detail" ),
    path('student-details/<str:pk>/', views.studentdetails  , name="student-details" ),
    
    path('student-update/<str:pk>/', views.studentupdate  , name="student-update" ),
    path('student-delete/<str:pk>/', views.studentdelete  , name="student-delete" ),
    
    
]
