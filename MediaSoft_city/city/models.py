from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'cities_table'
        verbose_name = 'city'
        verbose_name_plural = 'cities'

    def __str__(self):
        return self.name


class Street(models.Model):

    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shop(models.Model):

    name = models.CharField(max_length=50)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    house_num = models.IntegerField()
    opening_time = models.TimeField(auto_now=False, auto_now_add=False)
    closing_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.name
