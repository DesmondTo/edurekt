from django.db import models
from modules.models import Module


class Student(models.Model):
    matric_number = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    year = models.PositiveSmallIntegerField(blank=False, default=1)
    course = models.CharField(max_length=256, blank=False)

    module = models.ManyToManyField(Module, related_name= 'students', through='TakeModule')
    

    def __str__(self):
        return "{}:{}".format(self.name, self.matric_number)

class TakeModule(models.Model):
    student = models.ForeignKey(Student, on_delete=models.deletion.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.deletion.CASCADE)

    class Meta:
        unique_together = ('module', 'student')