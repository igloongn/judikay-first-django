from django.db import models

class FirstModel(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    humanrace=models.BooleanField(default=True)

    def __str__(self):
        return self.firstname
        

