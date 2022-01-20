from django.contrib import admin

from . import forms
from .models import Student, Teacher


class StudentAdmin(admin.ModelAdmin):
    form = forms.StudentForm
    list_display = "__all__"


admin.site.register(Teacher)
admin.site.register(Student)
