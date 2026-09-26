from django.db import models
from django.core.validators import MinLengthValidator


class Student(models.Model):
    name = models.CharField(max_length=100)


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Company(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(5)])
    location = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to="company_logos/", null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_approve_company", "can approve company"),
            ("can_delete_company", "can delete company"),
        ]

    def __str__(self):
        return self.name
