from django.db import models


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.code} ({self.city})"


class Flight(models.Model):
    # A foreign key which references another table
    # in this case it is referencing to Airport
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination= models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration= models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.origin} {self.destination}"


    # on_delete=models.CASCADE
    # it meeans when i have tables that are related to each other
    # sql needs some way of knowing what should happen if you delete something
    # models.CASCADE means if i ever delete an airport from the Airports Table
    #  it'll also delete any of the corresponding flights    

    # related_name
    # it is going to be ta way of accessing a relationship in the reverse order


class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")  

    def __str__(self):
        return f"{self.first} {self.last}"