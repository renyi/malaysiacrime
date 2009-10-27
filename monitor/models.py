from django.db import models

class Moniton(models.Model):
    """
    A monitoring unit. Consist of the monitored area and email.
    """
    email  = models.EmailField()
    north  = models.FloatField()
    east   = models.FloatField()
    south  = models.FloatField()
    west   = models.FloatField()
    zoom   = models.IntegerField()
    uuid       = models.CharField(max_length=32, default='', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.email
