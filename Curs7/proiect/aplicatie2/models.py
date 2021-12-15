from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from aplicatie1.models import Location


class Logs(models.Model):
    objects = None
    action_choices = (('created', 'created'),  # tip de date: tuple
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))

    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey('auth.User',
                             on_delete=models.CASCADE)  # fk - un utiliz poate avea mai multe loguri, CASCADE - cand se sterge un utiliz, toate inreg din celelalte tabele vor fi sterse
    action = models.CharField('Action', max_length=10, choices=action_choices)
    url = models.CharField('URL', max_length=100)  # url-ul pag pe care facem refresh


class Pontaj(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)


class Companies(models.Model):
    company_choices = (('SRL', 'S.R.L.'),
                       ('SA', 'S.A.'))

    name = models.CharField(max_length=100)
    website = models.CharField(max_length=80)
    company_type = models.CharField(max_length=5, choices=company_choices)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.company_type} {self.name}"


class UserExtend(User):

    customer = models.ForeignKey(Companies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.customer.name}"
