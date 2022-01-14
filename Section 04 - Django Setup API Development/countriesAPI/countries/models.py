from django.db import models
from django.db.models.expressions import F

# Create your models here.


class Countries(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')
    capital = models.CharField(max_length=50, blank=False, default='')

    def __str__(self) -> str:
        return self.name

class Meta:
    ordering = ('id',)
