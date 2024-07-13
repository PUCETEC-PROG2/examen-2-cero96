from django.db import models

# Create your models here.
# create pokemon from model set
 
class Movies(models.Model):
    name = models.CharField(max_length=30, null=False)
    MOVIES_TYPES = {
        ("M", "Miedo"),
        ("A", "Accion"),
        ("R", "Romance"),
        ("C", "Comedia"),
        ("T", "Terror")
    }
    type = models.CharField(max_length=30, choices=MOVIES_TYPES, null=False)
    director = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    año = models.DecimalField(null=False, default=1, max_digits=4, decimal_places=2)
    sinopsis = models.TextField(null=False,max_length=30)
    
    def __str__(self) -> str:
        return self.name