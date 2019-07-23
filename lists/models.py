from django.db import models
from django.urls import reverse

class List(models.Model):
    id = models.AutoField(primary_key=True, max_length=7)
    description = models.TextField(default='')

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField()
    list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True)
    #list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('list', 'text')
        ordering = ('id',)

    def __str__(self):
        return self.text
