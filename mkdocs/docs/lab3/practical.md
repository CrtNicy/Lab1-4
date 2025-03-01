# Practical Tasks - Air System

## Overview

Experiment 3 implements a complete flight booking system using Django REST Framework. The system includes flight management, passenger bookings, and a comment system.

## Task 1: API Development

### Requirements
1. Create RESTful API endpoints
2. Implement CRUD operations
3. Handle user authentication
4. Process JSON data

### Implementation

```python
# views.py
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            passenger = Passenger.objects.get(username=username, password=password)
            serializer = PassengerSerializer(passenger)
            return Response(serializer.data)
        except Passenger.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=401)
```

## Task 2: Data Modeling

### Requirements
1. Design database schema
2. Define model relationships
3. Implement validation rules
4. Handle data integrity

### Implementation

```python
# models.py
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=50)
    airline = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    flight_type = models.CharField(max_length=3, choices=[('ARR', 'Arrival'), ('DEP', 'Departure')])
    gate_number = models.CharField(max_length=10)

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
```

## Task 3: Frontend Integration

### Requirements
1. Create API endpoints
2. Handle CORS
3. Process API responses
4. Implement error handling

### Implementation

```javascript
// frontend.js
async function loginUser(username, password) {
    try {
        const response = await fetch('http://localhost:8000/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password }),
        });
        const data = await response.json();
        if (response.ok) {
            return data;
        } else {
            throw new Error(data.error);
        }
    } catch (error) {
        console.error('Login failed:', error);
        throw error;
    }
}

async function getFlights() {
    try {
        const response = await fetch('http://localhost:8000/api/flights/');
        const flights = await response.json();
        return flights;
    } catch (error) {
        console.error('Failed to fetch flights:', error);
        throw error;
    }
}
```

## Task 4: Testing

### API Testing

```python
# tests.py
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Flight, Passenger

class FlightAPITests(APITestCase):
    def setUp(self):
        self.flight = Flight.objects.create(
            flight_number='CA123',
            airline='Air China',
            departure_time='2024-02-28T10:00:00Z',
            arrival_time='2024-02-28T12:00:00Z',
            flight_type='DEP',
            gate_number='A1'
        )

    def test_list_flights(self):
        url = reverse('flight-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_booking(self):
        url = reverse('booking-list')
        data = {
            'flight': self.flight.id,
            'seat_number': 'A1'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
```

## Task 5: Documentation

### API Documentation

1. Flight Endpoints
```http
# List all flights
GET /api/flights/

# Create a new flight
POST /api/flights/
Content-Type: application/json

{
    "flight_number": "CA123",
    "airline": "Air China",
    "departure_time": "2024-02-28T10:00:00Z",
    "arrival_time": "2024-02-28T12:00:00Z",
    "flight_type": "DEP",
    "gate_number": "A1"
}
```

2. Booking Endpoints
```http
# Create a new booking
POST /api/bookings/
Content-Type: application/json

{
    "flight": 1,
    "seat_number": "A1"
}
```

## Deployment Steps

1. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

2. Create Superuser
```bash
python manage.py createsuperuser
```

3. Run Development Server
```bash
python manage.py runserver
```

## Security Considerations

1. Authentication
   - Implement user authentication
   - Secure password storage
   - Session management

2. Data Validation
   - Input sanitization
   - Data type validation
   - Business rule validation

3. Error Handling
   - Proper error messages
   - Status code usage
   - Exception handling

4. API Security
   - Rate limiting
   - CORS configuration
   - Token authentication 