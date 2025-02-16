from django.shortcuts import render,redirect
from django.views.generic import TemplateView,CreateView,ListView,DetailView

from app1.models import School
from app1.models import Student




class Home(TemplateView):
    template_name="home.html"

from django.urls import reverse_lazy
from app1.forms import SchoolForm
class AddSchool(CreateView):
    model=School
    # fields=['name','location','principal']
    form_class=SchoolForm
    template_name="addschool.html"
    success_url=reverse_lazy('home')

class AddStudent(CreateView):
    model=Student
    fields =['name','age','school']
    template_name="addstudent.html"
    success_url=reverse_lazy('home')

class SchoolList(ListView):
    model=School
    template_name="schoollist.html"
    context_object_name="school"

    def get_queryset(self):
        qs = super().get_queryset()
        queryset = qs.filter(location="trivandrum")
        return queryset


class SchoolDetail(DetailView):
    model=School
    template_name='schooldetail.html'
    context_object_name = "school"



class StudentDetail(ListView):
    model=Student
    template_name='studentdetail.html'
    context_object_name="student"

    def get_queryset(self):
        qs = super().get_queryset()
        queryset = qs.filter(school__location="trivandrum")
        return queryset

    def get_context_data(self):
        context=super().get_context_data
        context['name']='Arun'
        context['school']=School.objects.all()
        return context

from django.contrib.auth.models import User
class Register(CreateView):
    model=User
    fields=['username','password','email','first_name','last_name']
    template_name="register.html"
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']

        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('home')


from django.contrib.auth.views import LoginView
class Login(LoginView):
    template_name="login.html"

from django.views.generic import View
from django.contrib.auth import logout
class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('login')