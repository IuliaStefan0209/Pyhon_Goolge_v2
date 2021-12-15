from django.db import models

# Create your models here.

#ce e in paranteza se numeste mostenire
#Location e denumirea tabelului
class Location(models.Model):
    #city e string -> varchar in sql -> CharField in django
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    active = models.IntegerField(default=1)       #daca inregistrarea tb sa fie vizibila sau nu

    def __str__(self):                             #ne ajuta sa zicem ce vrem sa ne afiseze in mom in care apelam Location
        return f"{self.city} {self.country}"       #self - argumentul propriu al fct
