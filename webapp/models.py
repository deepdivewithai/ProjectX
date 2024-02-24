from django.db import models
from crm.settings import DEFAULT_AUTO_FIELD

class Record(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    address = models.CharField(max_length=300)

    city = models.CharField(max_length=20)
    province = models.CharField(max_length=20)

    country = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + "  " + self.last_name

