from django.db import models

# Create your models here.
class Gallery(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField()

    def __str__(self):
        return self.title
    
class TripDetail(models.Model):
    Coordinator = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    travel_partner = models.ForeignKey('TravelPartner', on_delete=models.SET_NULL, null=True)
    budget = models.IntegerField()
    locations = models.ManyToManyField('Destination')
    passengers = models.IntegerField()

    def __str__(self):
        locations_str = ', '.join(location.location for location in self.locations.all())
        return f"{locations_str}, {self.Coordinator}, {self.travel_partner}, {self.budget}, {self.passengers}, {self.start_date}-{self.end_date}"

class Destination(models.Model):
    location=models.CharField(max_length=100)
    def __str__(self):
        return self.location

class TravelPartner(models.Model):
    name=models.CharField(max_length=100)
    contact=models.IntegerField()
    place=models.CharField(max_length=100)
    logoname=models.CharField(max_length=100)
    partnerimage=models.ImageField()
    def __str__(self):
        return f"{self.name},{self.contact},{self.place},{self.logoname}"

class garage(models.Model):
    vehiclename=models.CharField(max_length=100)
    vehicleimage=models.ImageField()
    def __str__(self):
        return self.vehiclename