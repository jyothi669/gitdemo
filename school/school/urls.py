"""
URL configuration for school project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home.as_view(),name="home"),
    path('addschool',views.AddSchool.as_view(),name="addschool"),
    path('addstudent',views.AddStudent.as_view(),name="addstudent"),
    path('schoollist',views.SchoolList.as_view(),name="schoollist"),
    path('schooldetail/<int:pk>', views.SchoolDetail.as_view(), name="schooldetail"),
    path('studentdetail', views.StudentDetail.as_view(), name="studentdetail"),
    path('register', views.Register.as_view(), name="register"),
    path('login', views.Login.as_view(), name="login"),
    path('logout', views.Logout.as_view(), name="logout"),
]
