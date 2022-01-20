import pytest
from django.db import IntegrityError

from .forms import StudentForm
from .models import Student


@pytest.mark.parametrize(
    "age",
    [
        (9),
        (21),
    ],
)
def test_student_age(db, age):
    with pytest.raises(IntegrityError):
        Student.objects.create(first_name="Louis", last_name="Agyapong", age=age, classroom=100, teacher="Mr. Teye")


def test_student_form():
    data = {
        "first_name": "Louis",
        "last_name": "Agyapong",
        "age": 21,
        "classroom": 6,
        "teacher": "Mr. Teye",
    }
    form = StudentForm(data=data)
    assert False == form.is_valid()
