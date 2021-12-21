from django.db import models

# Create your models here.


class UrlMapping(models.Model):
    class Meta:
        db_table = 'URL_MAPPING'

    origin_url = models.CharField(max_length=300)
    shortener_url = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)
