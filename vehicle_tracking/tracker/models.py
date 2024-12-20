from django.db import models


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    current_latitude = models.FloatField()
    current_longitude = models.FloatField()

    def __str__(self):
        return self.name

class Journey(models.Model):
    vehicle_1 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='journeys_as_vehicle_1')
    vehicle_2 = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='journeys_as_vehicle_2')
    destination_latitude = models.FloatField()
    destination_longitude = models.FloatField()
    start_time = models.DateTimeField(auto_now_add=True)

