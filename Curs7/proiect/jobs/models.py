from django.db import models

# Create your models here.


class Job(models.Model):

    name = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey('aplicatie2.Companies', on_delete=models.CASCADE)
    active = models.IntegerField(default=1)

#a se realiza Create, Read, Update, Delete (CRUD) pt modulul de jobs.
#trebuie sa avem o validare in care sa nu existe job cu nume si customer identic