from django.shortcuts import render
from .models import *
from django.views import generic
# Create your views here.


class CourseList(generic.ListView):
    model  = Course
    


class CourseDetail(generic.DetailView):
    model  = Course