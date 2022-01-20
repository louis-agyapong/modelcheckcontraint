from django.contrib import admin

from . import forms
from .models import Student, Teacher


class StudentAdmin(admin.ModelAdmin):
    form = forms.StudentForm


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
