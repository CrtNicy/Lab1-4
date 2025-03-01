# Serializers Configuration

## Overview

Experiment 3 implements serializers using Django REST Framework for the flight booking system.

## Serializer Classes

### Flight Serializer

```python
from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = [
            'id', 'flight_number', 'airline',
            'departure_time', 'arrival_time',
            'flight_type', 'gate_number'
        ]
```

### Passenger Serializer

```python
from .models import Passenger

class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ['id', 'username', 'password', 'bookings']
```

### Booking Serializer

```python
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'passenger', 'flight', 'seat_number']
```

### Comment Serializer

```python
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id', 'flight', 'comment_text',
            'rating', 'commenter_name', 'comment_date'
        ]
```

## Serializer Features

1. Field Serialization
   - Model field mapping
   - Relationship handling
   - Custom field types
   - Field validation

2. Data Validation
   - Model validation
   - Field validation
   - Custom validators
   - Error handling

3. Nested Relationships
   - Foreign key serialization
   - Many-to-many serialization
   - Nested object creation
   - Related field handling

4. Data Formatting
   - JSON serialization
   - Date/time formatting
   - Field type conversion
   - Custom output formatting

## Usage Examples

### Creating Objects

```python
# Creating a flight
data = {
    'flight_number': 'CA123',
    'airline': 'Air China',
    'departure_time': '2024-02-28T10:00:00Z',
    'arrival_time': '2024-02-28T12:00:00Z',
    'flight_type': 'DEP',
    'gate_number': 'A1'
}
serializer = FlightSerializer(data=data)
if serializer.is_valid():
    flight = serializer.save()
```

### Updating Objects

```python
# Updating a booking
booking = Booking.objects.get(id=1)
data = {'seat_number': 'B12'}
serializer = BookingSerializer(booking, data=data, partial=True)
if serializer.is_valid():
    booking = serializer.save()
```

## Validation Examples

### Custom Field Validation

```python
class CommentSerializer(serializers.ModelSerializer):
    def validate_rating(self, value):
        if value < 1 or value > 10:
            raise serializers.ValidationError(
                "Rating must be between 1 and 10"
            )
        return value

    class Meta:
        model = Comment
        fields = '__all__'
```

### Object-Level Validation

```python
class BookingSerializer(serializers.ModelSerializer):
    def validate(self, data):
        # Check if seat is available
        if Booking.objects.filter(
            flight=data['flight'],
            seat_number=data['seat_number']
        ).exists():
            raise serializers.ValidationError(
                "This seat is already booked"
            )
        return data

    class Meta:
        model = Booking
        fields = '__all__'
```

## Response Formats

### Success Response

```json
{
    "id": 1,
    "flight_number": "CA123",
    "airline": "Air China",
    "departure_time": "2024-02-28T10:00:00Z",
    "arrival_time": "2024-02-28T12:00:00Z",
    "flight_type": "DEP",
    "gate_number": "A1"
}
```

### Error Response

```json
{
    "rating": ["Ensure this value is less than or equal to 10."],
    "seat_number": ["This seat is already booked"]
}
``` 