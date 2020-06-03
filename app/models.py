from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    credit=models.IntegerField(null=False)

    def __str__(self):
        return self.name
    def getname(self):
        return self.name