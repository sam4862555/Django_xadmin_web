from django.db import models

# Create your models here.

class CityList(models.Model):
    id = models.IntegerField(primary_key=True)
    city_code = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'city_list'


class UserTest(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'user_test'