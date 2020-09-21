from django.db import models
from modules.models import Module

# Create your models here.
class Lecturer(models.Model):
    staff_id = models.CharField(primary_key=True, max_length=9, blank=False)
    name = models.CharField(max_length=256, blank=False)
    department = models.CharField(max_length=256, blank=False)

    module = models.ForeignKey(Module, related_name = 'Lecturers', null = True, on_delete=models.SET_NULL)

    def __str__(self):
        return "{}:{}".format(self.staff_id, self.name)