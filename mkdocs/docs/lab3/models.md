# Models Configuration

## Overview

Experiment 3 implements the data models for a flight booking system using Django models. The system includes flights, passengers, bookings, and comments.

## Model Classes

### Flight Model

```python
from django.db import models

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
```

### Passenger Model

```python
class Passenger(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    bookings = models.ManyToManyField(Flight, through='Booking')

    def __str__(self):
        return self.username
```

### Booking Model

```python
class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.passenger.username} - {self.flight.flight_number}"
```

### Comment Model

```python
class Comment(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    comment_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])
    commenter_name = models.CharField(max_length=100)
    comment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.flight.flight_number} - {self.commenter_name}"
```

## Model Relationships

1. Flight - Passenger (Many-to-Many through Booking)
   - Passengers can book multiple flights
   - Flights can have multiple passengers
   - Booking model tracks seat assignments

2. Flight - Comment (One-to-Many)
   - Each flight can have multiple comments
   - Each comment belongs to one flight

## Field Types

1. Text Fields
   - CharField: For short text (flight numbers, names)
   - TextField: For longer text (comments)

2. Date/Time Fields
   - DateTimeField: For flight times
   - DateField: For comment dates

3. Relationship Fields
   - ForeignKey: For one-to-many relationships
   - ManyToManyField: For many-to-many relationships

4. Choice Fields
   - Flight type choices (ARR/DEP)
   - Rating choices (1-10)

## Model Features

1. String Representation
   - Custom __str__ methods
   - Human-readable output

2. Field Constraints
   - Maximum length limits
   - Unique constraints
   - Required fields

3. Automatic Fields
   - Auto-add dates
   - Auto-incrementing IDs

4. Data Validation
   - Field type validation
   - Choice field validation
   - Relationship integrity 