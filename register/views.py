from django.shortcuts import render, get_object_or_404
from django.views import  generic

from .models import Professor, Course, Student


def professor_list(request):
    professor_list = Professor.objects.order_by('-professor_name')
    context = {'professor_list': professor_list}
    return render(request,'register/professor_list.html', context)


def professor_detail(request, professor_id):
    professor = get_object_or_404(Professor, pk=professor_id)
    return render(request,'register/professor_detail.html', {'professor': professor})


def course_list(request):
    course_list = Course.objects.order_by('course_name')
    context = {'course_list': course_list}
    return render(request, 'register/course_list.html', context)


def course_detail(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request,'register/course_detail.html', {'course': course})


def student_list(request):
    student_list = Student.objects.order_by('student_name')
    context = {'student_list': student_list}
    return render(request, 'register/student_list.html', context)


def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    return render(request, 'register/student_detail.html', {'student': student})

