from django.conf.urls import url

from .import views

# app_name = 'register'
urlpatterns = [
    url(r'^$', views.professor_list, name='professor_list'),
    url(r'^professor_detail/(?P<professor_id>[0-9]+)/$', views.professor_detail, name='professor_detail'),
    url(r'^course_list/', views.course_list, name='course_list'),
    url(r'^course_detail/(?P<course_id>[0-9]+)/$', views.course_detail, name='course_detail'),

]
