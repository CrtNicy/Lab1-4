from django.db import models
from django.contrib.auth.models import User

class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    airline = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    FLIGHT_TYPES = (
        ('ARR', 'Arrival'),
        ('DEP', 'Departure')
    )
    flight_type = models.CharField(max_length=3, choices=FLIGHT_TYPES)
    gate_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.flight_number}"

class Passenger(models.Model):
    username = models.CharField(max_length=255, unique=True,null=False,default='username')
    password = models.CharField(max_length=255,null=False,default='password')
    bookings = models.ManyToManyField(Flight, through='Booking')

    def __str__(self):
        return self.username

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.passenger.username} - {self.flight.flight_number} - {self.seat_number}"

class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    comment_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    commenter_name = models.CharField(max_length=100)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight.flight_number} - {self.commenter_name} - {self.comment_date}"
