from django.db import models

class Caneta(models.Model):
    marca = models.CharField(max_length=80)
    cor = models.CharField(max_length=30)