from django.conf.urls import url

from .import views

# app_name = 'register'
urlpatterns = [
   url(r'^$', views.professor_list, name='professor_list'),
]