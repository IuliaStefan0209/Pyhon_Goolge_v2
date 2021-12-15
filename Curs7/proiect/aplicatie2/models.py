from django.db import models

# Create your models here.


class Logs(models.Model):
    objects = None
    action_choices = (('created', 'created'),             #tip de date: tuple
                      ('updated', 'updated'),
                      ('refresh', 'refresh'))


    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)              #fk - un utiliz poate avea mai multe loguri, CASCADE - cand se sterge un utiliz, toate inreg din celelalte tabele vor fi sterse
    action = models.CharField('Action', max_length=10, choices=action_choices)
    url = models.CharField('URL', max_length=100)                  #url-ul pag pe care facem refresh


class Pontaj(models.Model):

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)