from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=15)
    message = models.CharField(max_length=250)
