from django.db import models

class Constructor(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    championships = models.IntegerField(default=0)
    logo = models.ImageField(upload_to='constructors/', blank=True, null=True)

    def __str__(self):
        return self.name


class Driver(models.Model):
    constructor = models.ForeignKey(Constructor, on_delete=models.CASCADE, related_name='drivers')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    driver_number = models.PositiveIntegerField()
    country = models.CharField(max_length=100)
    driver_photo = models.ImageField(upload_to='drivers/photos/', blank=True, null=True)
    car_photo = models.ImageField(upload_to='drivers/cars/', blank=True, null=True)
    country_flag = models.ImageField(upload_to='drivers/flags/', blank=True, null=True)
    career_points = models.FloatField(default=0)
    highest_race_finish = models.CharField(max_length=20, blank=True)
    podiums = models.IntegerField(default=0)
    world_championships = models.IntegerField(default=0)
    dnfs = models.IntegerField(default=0)
    date_of_birth = models.DateField()
    place_of_birth = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
