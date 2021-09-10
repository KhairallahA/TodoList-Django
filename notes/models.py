from django.db import models
from django.urls import reverse

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField(null=False, blank=False)
    data  = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Note'

    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={'id': self.id})