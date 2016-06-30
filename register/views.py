from django.shortcuts import render
from django.views import  generic

from .models import Professor,Course,Student

class IndexView(generic.View):
    model = Professor
    template_name = 'register/index.html'




# Create your views here.
