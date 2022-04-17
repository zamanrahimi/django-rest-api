# create restApi - section 4

from django.contrib import admin
from django.urls import path, include
from .import views 

urlpatterns = [


    path('student/', views.student_list),
    path('student/<int:id>/', views.student_detail)
]
