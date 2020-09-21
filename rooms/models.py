from django.db import models

# Create your models here.
class Room(models.Model):
    code = models.CharField(primary_key=True, max_length=32, blank=False)
    name = models.CharField(max_length=256, blank=False)
    max_capacity = models.PositiveSmallIntegerField(blank=False)
    address = models.TextField(blank=False)

    def __str__(self):
        return "{}:{}".format(self.code, self.name)