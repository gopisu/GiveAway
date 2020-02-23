from django.db import models
from django.conf import settings
import Oddam.utils as utils


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    TYPE_CHOICES = (
        ('ORG', "Organizacja pozarządowa"),
        ('FUND', "Fundacja"),
        ('GAT', "Zbiórka lokalna")
    )
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=252)
    type = models.CharField(choices=TYPE_CHOICES, max_length=4, default='FUND')
    categories = models.ManyToManyField(Category)


class Donation(models.Model):
    quantity = models.PositiveIntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, related_name="institutionDonation", on_delete=models.CASCADE)
    address = models.CharField(max_length=252)
    phone_number = models.CharField(max_length=21)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=126)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="userDonation",
                             on_delete=models.SET(utils.get_sentinel_user), null=True, default=None)
