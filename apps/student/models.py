from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class Teacher(models.Model):
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    first_name = models.CharField(_("first name"), max_length=255)
    last_name = models.CharField(_("last name"), max_length=255)
    age = models.IntegerField(_("age"))
    classroom = models.IntegerField(_("classroom"))
    teacher = models.CharField(_("teacher"), max_length=255)

    class Meta:
        constraints = [models.CheckConstraint(check=Q(age__gte=10) & Q(age__lte=20), name="age_10_20")]
        verbose_name = _("student")
        verbose_name_plural = _("students")

    def clean(self):
        if self.age > 20 or self.age < 10:
            raise ValidationError({"age": _("Age must be less than 20")})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
