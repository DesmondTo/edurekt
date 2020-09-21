from django.db import models

from rooms.models import Room

# Create your models here.
class Module(models.Model):
    code = models.CharField(primary_key=True, max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    time = models.DateTimeField(blank=True, null = True)
    description = models.TextField(blank=True)

    room = models.OneToOneField(Room, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return "{}:{}".format(self.code, self.name)