from django.contrib import admin
from .models import Professor, Course, Student


class CourseInline(admin.TabularInline):
    model = Course
    extra = 3


# class ProfessorAdmin(admin.ModelAdmin):

    # inlines = [CourseInline]
    # list_display = ('')

admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Student)