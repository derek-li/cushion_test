from django.db import models

# Create your models here.
class Visitor(models.Model):

    address = models.CharField(max_length=255)
    date = models.DateTimeField()

    def __str__(self):
        return self.address + " " + str(self.date)