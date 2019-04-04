from django.db import models
from django.urls import reverse


class Shortcut(models.Model):
    """
        Model of shortcut, attribute short is the one we are heading to get
        It's built with host_name of website /id of shortcut
    """
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=500)
    short = models.URLField(max_length=100, blank=True)

    def get_absolute_url(self):
        return reverse('shortcut', args=[str(self.id)])

