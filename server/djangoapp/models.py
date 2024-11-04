from django.db import models
# from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# car make model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    # Other fields as needed
    def __str__(self):
        return self.name


# car model 
class CarModel(models.Model):
    # Many-to-One relationship
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("UTE", "Ute"),
        ("WAGON", "Wagon"),
        # Add more choices as required
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default="SUV")
    year = models.IntegerField(
        default=2023,
        validators=[MaxValueValidator(2023), MinValueValidator(2000)],
    )


    # Other fields as needed
    def __str__(self):
        return self.name
