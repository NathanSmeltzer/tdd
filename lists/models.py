from django.db import models

class List(models.Model):
    id = models.AutoField(primary_key=True, max_length=7)
    description = models.TextField(default='')

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)
