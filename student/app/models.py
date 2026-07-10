from django.db import models


# Create your models here.
class BaseModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    Email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Student(BaseModel):
    pass


class Teacher(BaseModel):
    pass


class NonTeachingStaff(BaseModel):
    pass
