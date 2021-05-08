from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 150)
    email = models.CharField(max_length= 300) 
    phone_number = models.IntegerField(max_length=10)
    desc = models.TextField()
    date = models.DateField()
    

    def __str__(self) -> str:
        return self.name
    