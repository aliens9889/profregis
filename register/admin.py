from django.contrib import admin
from .models import Professor, Course, Student


class CourseInline(admin.TabularInline):
    model = Course
    extra = 3


class ProfessorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['professor_name']}),
        ('Course', {'fields': ['course_name']}),
    ]

    inlines = [CourseInline]
    # list_display = ('')
