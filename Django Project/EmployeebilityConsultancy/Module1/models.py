from django.db import models

class date(models.Model):
    time12 = models.TextField(max_length=255)
    class Meta:
        db_table = "date"
# Create your models here.
