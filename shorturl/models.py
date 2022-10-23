from pyexpat import model
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models


class ShortUrl(models.Model):
    original_url = models.URLField(max_length = 800)
    short_url = models.CharField(max_length = 50)
    time_date_created = models.DateTimeField()


    def __str__(self) -> str:
        return  f"{ self.original_url }"


