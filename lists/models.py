from django.db import models

class Item(models.Model):
    text = models.TextField(default='')
    #list = model.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)

# class List(models.Model):
#     description =
#     list_id =
